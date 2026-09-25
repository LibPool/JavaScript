#!/usr/bin/env python3
"""Build the JavaScript/npm index commit directly from metadata JSONL.

The final layout matches tools/generate_index.py:

  node-v<major>/<package-dir>/<package-name>.md

The tree objects are constructed directly as loose objects instead of feeding
millions of filemodify commands to git fast-import, which avoids the
fast-import tree-phase bottleneck on the ~20 million entry npm snapshot.

Run inside WSL so the loose objects and record files live on ext4:

  python3 /mnt/d/Projects/LibPool/tools/build_js_git_objects.py \
    --meta-dir /mnt/d/Projects/LibPool/JavaScript_export_node/tools/cache/npm_meta_split \
    --export /mnt/d/Projects/LibPool/JavaScript_export_node \
    --source-repo /mnt/d/Projects/LibPool/JavaScript \
    --repo /root/js_snapshot.git
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import queue
import re
import shlex
import subprocess
import sys
import threading
import time
import zlib
from pathlib import Path


IDENTITY = "LibPool Bot <libpool@users.noreply.github.com>"
NODE_RELEASES = ["node-v18", "node-v20", "node-v22", "node-v24", "node-v26"]


def load_helpers(export_root: Path):
    path = export_root / "tools" / "generate_index.py"
    spec = importlib.util.spec_from_file_location("generate_index", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["generate_index"] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def sanitize_seg(seg: str, reserved: set[str]) -> str:
    seg = re.sub(r"[^A-Za-z0-9._@+-]", "-", seg)
    seg = re.sub(r"\.{2,}", "-", seg)
    seg = seg.rstrip(". ")
    if not seg:
        seg = "_"
    if seg.lower() in reserved:
        seg += "-pkg"
    return seg


def blob_oid(data: bytes) -> bytes:
    return hashlib.sha1(b"blob %d\x00" % len(data) + data).digest()


def tree_oid(raw: bytes) -> bytes:
    return hashlib.sha1(b"tree %d\x00" % len(raw) + raw).digest()


def tree_sort_key(entry: tuple[bytes, bytes, bytes]) -> tuple[bytes, bytes, bytes]:
    mode, name, _oid = entry
    return (name + (b"/" if mode == b"40000" else b""), mode, name)


def write_tree(entries: list[tuple[bytes, bytes, bytes]], store: "ObjectStore") -> bytes:
    entries.sort(key=tree_sort_key)
    raw = b"".join(mode + b" " + name + b"\x00" + oid for mode, name, oid in entries)
    oid = tree_oid(raw)
    store.write(oid, b"tree %d\x00" % len(raw), raw)
    return oid


def read_tree_entries(store: "ObjectStore", oid: bytes) -> list[tuple[bytes, bytes, bytes]]:
    """Read a tree object back from the store (loose or packed)."""
    def via_git() -> bytes:
        return subprocess.check_output(
            ["git", "-C", str(store.root.parent), "cat-file", "tree", oid.hex()]
        )

    path = store.root / oid.hex()[:2] / oid.hex()[2:]
    try:
        raw_compressed = path.read_bytes()
    except FileNotFoundError:
        raw = via_git()
    else:
        try:
            raw = zlib.decompress(raw_compressed)
        except zlib.error:
            raw = via_git()
    _, payload = raw.split(b"\x00", 1)
    entries: list[tuple[bytes, bytes, bytes]] = []
    i = 0
    while i < len(payload):
        sp = payload.index(b" ", i)
        mode = payload[i:sp]
        nul = payload.index(b"\x00", sp + 1)
        name = payload[sp + 1 : nul]
        entries.append((mode, name, payload[nul + 1 : nul + 21]))
        i = nul + 21
    return entries


def merge_root_entry(
    store: "ObjectStore", old: bytes, new: bytes
) -> bytes:
    """Combine two top-level trees for the same directory name."""
    merged: dict[bytes, tuple[bytes, bytes]] = {
        name: (mode, oid) for mode, name, oid in read_tree_entries(store, old)
    }
    for mode, name, oid in read_tree_entries(store, new):
        merged[name] = (mode, oid)
    return write_tree(
        [(mode, name, oid) for name, (mode, oid) in merged.items()],
        store,
    )


class ObjectStore:
    def __init__(self, root: Path):
        self.root = root
        self.locks = [threading.Lock() for _ in range(256)]
        for i in range(256):
            (root / f"{i:02x}").mkdir(parents=True, exist_ok=True)

    def write(self, oid: bytes, header: bytes, raw: bytes) -> None:
        hexdigest = oid.hex()
        lock = self.locks[int(hexdigest[:2], 16)]
        target = self.root / hexdigest[:2] / hexdigest[2:]
        if target.exists():
            return
        data = zlib.compress(header + raw, 6)
        tmp = target.with_name(target.name + f".tmp{threading.get_ident()}")
        with lock:
            if target.exists():
                return
            tmp.write_bytes(data)
            os.replace(tmp, target)


def node_major(release: str) -> int:
    return int(release.replace("node-v", ""))


def worker(
    gen,
    store: ObjectStore,
    task_q: queue.Queue,
    done_q: queue.Queue,
    stats: dict[str, int],
    stats_lock: threading.Lock,
) -> None:
    while True:
        task = task_q.get()
        if task is None:
            return
        seq, line = task
        try:
            item = json.loads(line)
        except Exception:
            with stats_lock:
                stats["malformed"] += 1
            done_q.put((seq, "", None, 0))
            continue
        name = item.get("name") or ""
        version = item.get("version") or ""
        if not name or not version:
            with stats_lock:
                stats["no_version"] += 1
            done_q.put((seq, name, None, 0))
            continue
        lib = gen.JsLib(
            name=name,
            tags=item.get("tags") or [],
            version=version,
            description=item.get("description") or "",
            homepage=item.get("homepage") or "",
            repository=item.get("repository") or "",
            engines_node=item.get("engines_node") or "",
            versions=item.get("versions") or [],
            version_count=int(item.get("version_count") or 0),
        )
        baseline = gen.node_major_baseline(lib.engines_node) or 18
        data = gen.readme_md(lib).encode("utf-8")
        blob = blob_oid(data)
        store.write(blob, b"blob %d\x00" % len(data), data)
        parts = [sanitize_seg(p, gen.WINDOWS_RESERVED) for p in name.split("/")]
        parts = [p for p in parts if p]
        if not parts:
            with stats_lock:
                stats["empty_path"] += 1
            done_q.put((seq, name, None, 0))
            continue
        filename = parts[-1] + ".md"
        dir_raw = b"100644 " + filename.encode("ascii") + b"\x00" + blob
        dir_oid = tree_oid(dir_raw)
        store.write(dir_oid, b"tree %d\x00" % len(dir_raw), dir_raw)
        blob_hex = blob.hex()
        dir_hex = dir_oid.hex()
        results = []
        for release in NODE_RELEASES:
            if node_major(release) < baseline:
                continue
            topseg = parts[0]
            pkgdir = "" if len(parts) == 1 else parts[-1]
            results.append((release, topseg, pkgdir, filename, blob_hex, dir_hex))
        done_q.put((seq, name, results, 1))


def build_release_tree(
    release: str,
    rec_path: Path,
    work_dir: Path,
    store: ObjectStore,
    threads: int,
) -> bytes:
    sorted_path = work_dir / f"{release}.records.sorted"
    env = dict(os.environ, LC_ALL="C")
    subprocess.run(
        [
            "sort",
            "-t",
            "\t",
            "-k1,1",
            "-k2,2",
            "-k3,3",
            "-k4,4",
            "-o",
            str(sorted_path),
            str(rec_path),
        ],
        check=True,
        env=env,
    )

    root_entries: dict[str, bytes] = {}
    dirs: list[tuple[str, bytes]] = []
    files: list[tuple[str, bytes]] = []
    current_top: str | None = None
    prev_key: tuple[str, str] | None = None
    pkg_files: list[tuple[str, bytes, bytes]] = []

    def append_pkg_dir() -> None:
        nonlocal prev_key, pkg_files
        if prev_key is None or not pkg_files:
            return
        pkgdir = prev_key[1]
        if not pkgdir:
            return
        if len(pkg_files) == 1:
            filename, blob, dir_oid = pkg_files[0]
            raw = (
                b"100644 " + filename.encode("ascii") + b"\x00" + blob
            )
            store.write(dir_oid, b"tree %d\x00" % len(raw), raw)
            oid = dir_oid
        else:
            oid = write_tree(
                [
                    (b"100644", filename.encode("ascii"), blob)
                    for filename, blob, _dir_oid in pkg_files
                ],
                store,
            )
        dirs.append((pkgdir, oid))
        pkg_files = []

    def finalize_top() -> None:
        nonlocal dirs, files
        if dirs or files:
            assert current_top is not None
            entries = [
                (b"40000", name.encode("ascii"), oid) for name, oid in dirs
            ] + [
                (b"100644", name.encode("ascii"), oid) for name, oid in files
            ]
            oid = write_tree(
                entries,
                store,
            )
            previous = root_entries.get(current_top)
            if previous is None:
                root_entries[current_top] = oid
            else:
                print(
                    f"  WARNING duplicate top {current_top!r} "
                    f"old={previous.hex()} new={oid.hex()}",
                    file=sys.stderr,
                    flush=True,
                )
                root_entries[current_top] = merge_root_entry(
                    store, previous, oid
                )
            dirs = []
            files = []

    processed = 0
    with sorted_path.open(encoding="ascii") as fh:
        for line in fh:
            fields = line.rstrip("\n").split("\t")
            if len(fields) != 5:
                continue
            topseg, pkgdir, filename, blob_hex, dir_hex = fields
            key = (topseg, pkgdir)
            if key != prev_key:
                append_pkg_dir()
                prev_key = key
                pkg_files = []
                if topseg != current_top:
                    finalize_top()
                    current_top = topseg
            if pkgdir:
                pkg_files.append(
                    (
                        filename,
                        bytes.fromhex(blob_hex),
                        bytes.fromhex(dir_hex),
                    )
                )
            else:
                files.append((filename, bytes.fromhex(blob_hex)))
            processed += 1
            if processed % 500000 == 0:
                print(
                    f"  {release} processed {processed:,} records",
                    flush=True,
                )
        append_pkg_dir()
        finalize_top()
    return write_tree(
        [
            (b"40000", name.encode("ascii"), oid)
            for name, oid in root_entries.items()
        ],
        store,
    )


def git_rev(repo: Path, rev: str) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", rev],
            text=True,
        ).strip()
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"cannot resolve {rev} in {repo}") from exc
    if not out:
        raise RuntimeError(f"cannot resolve {rev} in {repo}")
    return out


def git_rev_or_none(repo: Path, rev: str) -> str | None:
    try:
        return git_rev(repo, rev)
    except RuntimeError:
        return None


def count_objects(repo: Path, rev: str, path: str | None = None) -> int:
    cmd = f"git -C {shlex.quote(str(repo))} ls-tree -r --name-only {shlex.quote(rev)}"
    if path:
        cmd += f" {shlex.quote(path)}"
    out = subprocess.check_output(["bash", "-lc", cmd + " | wc -l"], text=True)
    return int(out.strip())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta-dir", required=True)
    ap.add_argument("--export", required=True)
    ap.add_argument("--source-repo", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--message", default="Add full npm index snapshot")
    args = ap.parse_args()

    meta_dir = Path(args.meta_dir).resolve()
    export = Path(args.export).resolve()
    source = Path(args.source_repo).resolve()
    repo = Path(args.repo).resolve()
    gen = load_helpers(export)

    if not (repo / "objects").exists():
        subprocess.run(
            ["git", "init", "--bare", "-b", "main", str(repo)],
            check=True,
        )
    existing_main = git_rev_or_none(repo, "refs/heads/main")
    if existing_main is None:
        subprocess.run(
            [
                "git",
                "-C",
                str(repo),
                "fetch",
                str(source),
                "refs/heads/main:refs/heads/main",
            ],
            check=True,
        )
    parent_hex = existing_main or git_rev(source, "refs/heads/main")
    gitignore_hex = git_rev_or_none(source, "refs/heads/main:.gitignore")
    tools_hex = git_rev_or_none(source, "refs/heads/main:tools")
    readme_bytes = (export / "README.md").read_bytes()
    readme_oid = blob_oid(readme_bytes)

    store = ObjectStore(repo / "objects")
    work_dir = repo.parent / (repo.name + ".work")
    work_dir.mkdir(parents=True, exist_ok=True)
    record_paths = {r: work_dir / f"{r}.records" for r in NODE_RELEASES}
    rec_fhs = {
        r: p.open("w", encoding="ascii", newline="\n") for r, p in record_paths.items()
    }

    task_q: queue.Queue = queue.Queue(maxsize=4096)
    done_q: queue.Queue = queue.Queue()
    stats = {
        "malformed": 0,
        "no_version": 0,
        "empty_path": 0,
        "records_written": 0,
        "collision_suffix": 0,
        "collision_skip": 0,
    }
    stats_lock = threading.Lock()
    threads = [
        threading.Thread(
            target=worker,
            args=(gen, store, task_q, done_q, stats, stats_lock),
            daemon=True,
        )
        for _ in range(args.workers)
    ]
    for t in threads:
        t.start()

    meta_parts: list[Path] = []
    for dirpath, _, filenames in os.walk(meta_dir):
        for fn in sorted(filenames):
            if fn.startswith("npm_meta_"):
                meta_parts.append(Path(dirpath) / fn)
    meta_parts.sort(key=lambda p: (p.parent.name, p.name))
    print(f"metadata parts: {len(meta_parts)}", flush=True)

    next_seq = 0
    enqueued = 0
    pending_results: dict[int, tuple[str, list | None, int]] = {}
    package_count = 0
    last_progress = 0

    def handle(seq: int, name: str, results: list | None, valid: int) -> None:
        nonlocal package_count, last_progress
        if valid != 1 or not results:
            return
        package_count += 1
        for release, topseg, pkgdir, filename, blob_hex, dir_hex in results:
            rel = "/".join(x for x in (release, topseg, pkgdir, filename) if x)
            key = rel.lower()
            old = seen[release].get(key)
            if old is None:
                seen[release][key] = name
                rec_fhs[release].write(
                    f"{topseg}\t{pkgdir}\t{filename}\t{blob_hex}\t{dir_hex}\n"
                )
                stats["records_written"] += 1
            elif old == name:
                continue
            else:
                digest = hashlib.sha1(name.encode("utf-8")).hexdigest()[:8]
                newfn = f"{filename[:-3]}-{digest}.md"
                newrel = f"{release}/{topseg}/{pkgdir}/{newfn}"
                newkey = newrel.lower()
                if newkey in seen[release]:
                    stats["collision_skip"] += 1
                    continue
                seen[release][newkey] = name
                newraw = (
                    b"100644 " + newfn.encode("ascii") + b"\x00" + bytes.fromhex(blob_hex)
                )
                newdir = tree_oid(newraw)
                store.write(newdir, b"tree %d\x00" % len(newraw), newraw)
                rec_fhs[release].write(
                    f"{topseg}\t{pkgdir}\t{newfn}\t{blob_hex}\t{newdir.hex()}\n"
                )
                stats["records_written"] += 1
                stats["collision_suffix"] += 1
        if package_count // 100000 > last_progress:
            last_progress = package_count // 100000
            print(
                f"  packages {package_count:,} entries {stats['records_written']:,}",
                flush=True,
            )

    def pump() -> None:
        nonlocal next_seq
        while True:
            try:
                seq, name, results, valid = done_q.get_nowait()
            except queue.Empty:
                break
            pending_results[seq] = (name, results, valid)
        while next_seq in pending_results:
            name, results, valid = pending_results.pop(next_seq)
            handle(next_seq, name, results, valid)
            next_seq += 1

    for part_idx, part in enumerate(meta_parts, 1):
        print(f"processing {part} ({part_idx}/{len(meta_parts)})", flush=True)
        seen = {r: {} for r in NODE_RELEASES}
        with part.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if not line.strip():
                    continue
                task_q.put((enqueued, line))
                enqueued += 1
                pump()
        while next_seq < enqueued:
            try:
                seq, name, results, valid = done_q.get(timeout=1.0)
            except queue.Empty:
                continue
            pending_results[seq] = (name, results, valid)
            while next_seq in pending_results:
                name, results, valid = pending_results.pop(next_seq)
                handle(next_seq, name, results, valid)
                next_seq += 1

    for _ in threads:
        task_q.put(None)
    for t in threads:
        t.join(timeout=5)
    for fh in rec_fhs.values():
        fh.close()

    print(
        "records: "
        + ", ".join(f"{r}={p.stat().st_size:,} bytes" for r, p in record_paths.items()),
        flush=True,
    )
    print(
        "stats: "
        + ", ".join(f"{k}={v:,}" for k, v in sorted(stats.items())),
        flush=True,
    )

    release_roots: dict[str, bytes] = {}
    for release in NODE_RELEASES:
        print(f"building {release} tree", flush=True)
        release_roots[release] = build_release_tree(
            release,
            record_paths[release],
            work_dir,
            store,
            max(8, args.workers),
        )
        print(f"  {release} root {release_roots[release].hex()}", flush=True)

    store.write(readme_oid, b"blob %d\x00" % len(readme_bytes), readme_bytes)
    root_entries: list[tuple[bytes, bytes, bytes]] = [
        (b"100644", b"README.md", readme_oid),
    ]
    if gitignore_hex:
        root_entries.append((b"100644", b".gitignore", bytes.fromhex(gitignore_hex)))
    root_entries += [
        (b"40000", release.encode("ascii"), release_roots[release])
        for release in NODE_RELEASES
    ]
    if tools_hex:
        root_entries.append((b"40000", b"tools", bytes.fromhex(tools_hex)))
    root_tree = write_tree(root_entries, store)
    print(f"repo root tree {root_tree.hex()}", flush=True)

    msg = args.message.encode("utf-8")
    stamp = int(time.time())
    commit_raw = (
        b"tree " + root_tree.hex().encode("ascii") + b"\n"
        b"parent " + parent_hex.encode("ascii") + b"\n"
        b"author " + IDENTITY.encode("ascii") + b" " + str(stamp).encode("ascii") + b" +0800\n"
        b"committer " + IDENTITY.encode("ascii") + b" " + str(stamp).encode("ascii") + b" +0800\n"
        b"\n" + msg
    )
    commit_oid = hashlib.sha1(b"commit %d\x00" % len(commit_raw) + commit_raw).digest()
    store.write(commit_oid, b"commit %d\x00" % len(commit_raw), commit_raw)
    subprocess.run(
        ["git", "-C", str(repo), "update-ref", "refs/heads/main", commit_oid.hex()],
        check=True,
    )
    print(f"commit {commit_oid.hex()}", flush=True)

    print(f"total files in HEAD tree: {count_objects(repo, 'HEAD'):,}", flush=True)
    for release in NODE_RELEASES:
        print(
            f"  {release}: {count_objects(repo, 'HEAD', release):,}",
            flush=True,
        )
    print(
        subprocess.check_output(
            ["git", "-C", str(repo), "count-objects", "-v"],
            text=True,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
