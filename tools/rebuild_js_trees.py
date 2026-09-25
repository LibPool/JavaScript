#!/usr/bin/env python3
"""Rebuild release trees from existing npm record files and commit them.

The regular builder (build_js_git_objects.py) can regenerate record files while
crawling metadata, which is unnecessary when the .records files already exist.
This helper reuses the exact tree-building logic on those existing records so a
clean snapshot can be rebuilt without re-downloading or re-processing metadata.

Usage (inside WSL, so objects live on ext4):

  python3 /mnt/d/Projects/LibPool/tools/rebuild_js_trees.py \
    --records-dir /root/js_snapshot.git.work \
    --export /mnt/d/Projects/LibPool/JavaScript_export_node \
    --source-repo /mnt/d/Projects/LibPool/JavaScript \
    --repo /root/js_snapshot2.git \
    --threads 16
"""

from __future__ import annotations

import argparse
import importlib.util
import pathlib
import subprocess
import sys
import time


def load_existing_objects(repo: pathlib.Path) -> set[bytes] | None:
    """Return all object ids already known to the repo, or None if absent."""
    try:
        out = subprocess.check_output(
            [
                "git",
                "-C",
                str(repo),
                "cat-file",
                "--batch-all-objects",
                "--batch-check=%(objectname)",
            ],
        )
    except subprocess.CalledProcessError:
        return None
    return {bytes.fromhex(line) for line in out.split()}


class ExistingAwareObjectStore:
    """Wrap the regular object store and skip objects already known to git."""

    def __init__(self, root: pathlib.Path, existing: set[bytes]):
        self.store = None
        self.root = root
        self.existing = existing

    def write(self, oid: bytes, header: bytes, raw: bytes) -> None:
        if oid in self.existing:
            return
        if self.store is None:
            # Deferred import keeps this file importable without the builder.
            import importlib.util

            mod = load_builder()
            self.store = mod.ObjectStore(self.root)
        self.store.write(oid, header, raw)


def load_builder():
    candidates = [
        pathlib.Path("/mnt/d/Projects/LibPool/tools/build_js_git_objects.py"),
        pathlib.Path(r"D:\Projects\LibPool\tools\build_js_git_objects.py"),
    ]
    path = next(p for p in candidates if p.exists())
    spec = importlib.util.spec_from_file_location("build_js_git_objects", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["build_js_git_objects"] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--records-dir", required=True)
    ap.add_argument("--export", required=True)
    ap.add_argument("--source-repo", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--threads", type=int, default=16)
    ap.add_argument("--message", default="Add clean full npm index snapshot")
    args = ap.parse_args()

    mod = load_builder()
    records_dir = pathlib.Path(args.records_dir).resolve()
    export = pathlib.Path(args.export).resolve()
    source = pathlib.Path(args.source_repo).resolve()
    repo = pathlib.Path(args.repo).resolve()

    if not (repo / "objects").exists():
        import subprocess

        subprocess.run(
            ["git", "init", "--bare", "-b", "main", str(repo)],
            check=True,
        )
    existing_main = mod.git_rev_or_none(repo, "refs/heads/main")
    if existing_main is None:
        import subprocess

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
    parent_hex = existing_main or mod.git_rev(source, "refs/heads/main")
    gitignore_hex = mod.git_rev_or_none(source, "refs/heads/main:.gitignore")
    tools_hex = mod.git_rev_or_none(source, "refs/heads/main:tools")
    readme_bytes = (export / "README.md").read_bytes()

    store = mod.ObjectStore(repo / "objects")
    existing = load_existing_objects(repo)
    if existing is not None:
        store = ExistingAwareObjectStore(repo / "objects", existing)
    release_roots: dict[str, bytes] = {}
    for release in mod.NODE_RELEASES:
        rec = records_dir / f"{release}.records"
        if not rec.exists():
            raise SystemExit(f"missing records: {rec}")
        print(f"building {release} tree", flush=True)
        release_roots[release] = mod.build_release_tree(
            release,
            rec,
            records_dir,
            store,
            max(8, args.threads),
        )
        print(f"  {release} root {release_roots[release].hex()}", flush=True)

    readme_oid = mod.blob_oid(readme_bytes)
    store.write(readme_oid, b"blob %d\x00" % len(readme_bytes), readme_bytes)
    root_entries: list[tuple[bytes, bytes, bytes]] = [
        (b"100644", b"README.md", readme_oid),
    ]
    if gitignore_hex:
        root_entries.append((b"100644", b".gitignore", bytes.fromhex(gitignore_hex)))
    root_entries += [
        (b"40000", release.encode("ascii"), release_roots[release])
        for release in mod.NODE_RELEASES
    ]
    if tools_hex:
        root_entries.append((b"40000", b"tools", bytes.fromhex(tools_hex)))
    root_tree = mod.write_tree(root_entries, store)
    print(f"repo root tree {root_tree.hex()}", flush=True)

    msg = args.message.encode("utf-8")
    stamp = int(time.time())
    commit_raw = (
        b"tree " + root_tree.hex().encode("ascii") + b"\n"
        b"parent " + parent_hex.encode("ascii") + b"\n"
        b"author " + mod.IDENTITY.encode("ascii") + b" " + str(stamp).encode("ascii") + b" +0800\n"
        b"committer " + mod.IDENTITY.encode("ascii") + b" " + str(stamp).encode("ascii") + b" +0800\n"
        b"\n" + msg
    )
    import hashlib

    commit_oid = hashlib.sha1(
        b"commit %d\x00" % len(commit_raw) + commit_raw
    ).digest()
    store.write(commit_oid, b"commit %d\x00" % len(commit_raw), commit_raw)

    import subprocess

    subprocess.run(
        ["git", "-C", str(repo), "update-ref", "refs/heads/main", commit_oid.hex()],
        check=True,
    )
    print(f"commit {commit_oid.hex()}", flush=True)
    print(f"total files in HEAD tree: {mod.count_objects(repo, 'HEAD'):,}", flush=True)
    for release in mod.NODE_RELEASES:
        print(
            f"  {release}: {mod.count_objects(repo, 'HEAD', release):,}",
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
