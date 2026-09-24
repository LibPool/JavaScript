#!/usr/bin/env python3
"""Download lean metadata for every current npm package id.

The full id list is produced by crawl_current_ids.py.  This script walks that
list with several worker processes, fetches each package document from the
public npm registry, and stores only the fields needed for the LibPool README
files in JSONL parts.

Run from the repo root:
    python tools/crawl_npm_meta.py --workers 16 --batch 20000
"""

from __future__ import annotations

import argparse
import json
import queue
import socket
import sys
import threading
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import urllib3.util.connection as _u3c
import requests


# Some networks leave IPv6 connections to the npm CDN half-open with no
# response and, on Windows, no socket timeout. Prefer IPv4 for reliability.
_u3c.allowed_gai_family = lambda: socket.AF_INET

USER_AGENT = "LibPool-Indexer/1.0 (+https://github.com/LibPool)"


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default="tools/cache/npm_current_ids.txt")
    ap.add_argument("--meta-dir", default="tools/cache/npm_meta_parts")
    ap.add_argument("--state", default="tools/cache/npm_meta_state.json")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--batch", type=int, default=20000)
    ap.add_argument("--max-requests", type=int, default=0)
    ap.add_argument("--seed-cache", default="tools/cache/npm.json")
    ap.add_argument("--registry", default="https://registry.npmjs.org")
    return ap.parse_args()


def load_seed_cache(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {k: v for k, v in data.items() if isinstance(v, dict)}


def extract_meta(name: str, data: dict) -> dict | None:
    if not isinstance(data, dict) or not data.get("name"):
        return None
    dist_tags = data.get("dist-tags") or {}
    versions = data.get("versions") or {}
    latest = dist_tags.get("latest") or ""
    meta = versions.get(latest) or {}
    if not meta and versions:
        meta = versions[next(iter(versions))]
    if not isinstance(meta, dict):
        meta = {}
    repo = meta.get("repository")
    repository = ""
    if isinstance(repo, dict):
        repository = str(repo.get("url") or "")
    elif isinstance(repo, str):
        repository = repo.strip()
    engines = meta.get("engines")
    engine_node = ""
    if isinstance(engines, dict):
        engine_node = str(engines.get("node") or "")
    elif isinstance(engines, str):
        engine_node = engines.strip()
    elif isinstance(engines, list):
        parts = [str(e) for e in engines]
        engine_node = ", ".join(parts)
    keywords = meta.get("keywords")
    tags = []
    if isinstance(keywords, list):
        tags = [str(k).strip() for k in keywords if str(k).strip()]
    elif isinstance(keywords, str) and keywords.strip():
        tags = [keywords.strip()]
    version_list = list(versions.keys())
    kept = version_list[-50:]
    return {
        "name": str(data.get("name")),
        "version": latest,
        "versions": kept,
        "version_count": len(version_list),
        "description": str(meta.get("description") or "").strip(),
        "homepage": str(meta.get("homepage") or "").strip(),
        "repository": repository.strip(),
        "engines_node": engine_node.strip(),
        "tags": tags,
    }


def main() -> int:
    args = parse_args()
    ids_path = Path(args.ids)
    meta_dir = Path(args.meta_dir)
    state_path = Path(args.state)
    meta_dir.mkdir(parents=True, exist_ok=True)
    if not ids_path.exists():
        print(f"id list not found: {ids_path}", file=sys.stderr)
        return 2

    seed_cache = load_seed_cache(Path(args.seed_cache))

    done_names: set[str] = set()
    if meta_dir.exists():
        for part in sorted(meta_dir.glob("npm_meta_*.jsonl")):
            with part.open(encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    try:
                        row = json.loads(line)
                        if row.get("name"):
                            done_names.add(str(row["name"]))
                    except Exception:
                        pass
    print(f"Already fetched: {len(done_names):,} package names", flush=True)

    with ids_path.open(encoding="utf-8", errors="replace") as fh:
        names = [line.strip() for line in fh if line.strip()]
    total = len(names)
    print(f"Loaded {total:,} npm package ids from {ids_path}", flush=True)

    batches: list[tuple[int, list[str]]] = []
    for start in range(0, total, args.batch):
        batches.append((start, names[start : start + args.batch]))

    state: dict = {}
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except Exception:
            state = {}
    done = set(int(x) for x in state.get("done", []))
    pending = [(start, chunk) for start, chunk in batches if start not in done]
    print(f"Pending batches: {len(pending)}/{len(batches)}", flush=True)

    lock = threading.Lock()
    stats = {"fetched": 0, "seed": 0, "failed": 0, "requests": 0, "skipped": 0}
    fail_path = meta_dir / "failures.jsonl"

    def save_state() -> None:
        tmp = state_path.with_suffix(".tmp")
        tmp.write_text(
            json.dumps({"done": sorted(done), "updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}),
            encoding="utf-8",
        )
        tmp.replace(state_path)

    def worker(worker_id: int) -> None:
        part_path = meta_dir / f"npm_meta_{worker_id:02d}.jsonl"
        session = requests.Session()
        session.headers["User-Agent"] = USER_AGENT
        local_done: list[int] = []

        def process_batch(start: int, chunk: list[str]) -> None:
            with lock:
                out = part_path.open("a", encoding="utf-8", newline="\n")
            try:
                for name in chunk:
                    if args.max_requests and stats["requests"] >= args.max_requests:
                        break
                    if name in done_names:
                        with lock:
                            stats["skipped"] += 1
                        continue
                    with lock:
                        stats["requests"] += 1
                    cached = seed_cache.get(name)
                    if cached:
                        meta = {
                            "name": cached.get("name") or name,
                            "version": cached.get("version", ""),
                            "versions": (cached.get("versions") or [])[-50:],
                            "version_count": len(cached.get("versions") or []),
                            "description": cached.get("description", ""),
                            "homepage": cached.get("homepage", ""),
                            "repository": cached.get("repository", ""),
                            "engines_node": cached.get("engines_node", ""),
                            "tags": cached.get("tags", []),
                        }
                        out.write(json.dumps(meta, ensure_ascii=False, separators=(",", ":")) + "\n")
                        with lock:
                            stats["seed"] += 1
                        continue
                    url = f"{args.registry}/{urllib.parse.quote(name, safe='@/')}"
                    data = None
                    last_exc: Exception | None = None
                    for attempt in range(8):
                        try:
                            resp = session.get(url, timeout=20)
                            if resp.status_code == 404:
                                data = {}
                                break
                            if resp.status_code in (429, 500, 502, 503, 504):
                                raise RuntimeError(f"HTTP {resp.status_code}")
                            resp.raise_for_status()
                            data = resp.json()
                            break
                        except Exception as exc:
                            last_exc = exc
                            time.sleep(1 + attempt * 3)
                    meta = extract_meta(name, data) if data else None
                    if meta:
                        out.write(json.dumps(meta, ensure_ascii=False, separators=(",", ":")) + "\n")
                        with lock:
                            stats["fetched"] += 1
                    else:
                        if data is None:
                            with lock:
                                stats["failed"] += 1
                            with fail_path.open("a", encoding="utf-8", newline="\n") as fail_out:
                                fail_out.write(
                                    json.dumps({"name": name, "error": str(last_exc)}, ensure_ascii=False) + "\n"
                                )
            finally:
                out.close()
            local_done.append(start)

        try:
            while True:
                try:
                    start, chunk = work_queue.get_nowait()
                except queue.Empty:
                    break
                process_batch(start, chunk)
                with lock:
                    done.add(start)
                    if len(done) % 10 == 0:
                        save_state()
                if args.max_requests and stats["requests"] >= args.max_requests:
                    break
        except Exception as exc:
            print(f"worker {worker_id} stopped: {exc}", flush=True)

        with lock:
            save_state()
            print(
                f"worker {worker_id}: done={len(local_done)} fetches={stats['fetched']:,} "
                f"seed={stats['seed']:,} skipped={stats['skipped']:,} "
                f"failed={stats['failed']:,} requests={stats['requests']:,}",
                flush=True,
            )

    threads = [threading.Thread(target=worker, args=(i,), daemon=True) for i in range(args.workers)]
    work_queue = queue.Queue()
    for item in pending:
        work_queue.put(item)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(
        f"Final: fetched={stats['fetched']:,} seed={stats['seed']:,} failed={stats['failed']:,} "
        f"skipped={stats['skipped']:,} requests={stats['requests']:,} done_batches={len(done)}/{len(batches)}",
        flush=True,
    )
    return 0 if len(done) >= len(batches) else 1


if __name__ == "__main__":
    raise SystemExit(main())
