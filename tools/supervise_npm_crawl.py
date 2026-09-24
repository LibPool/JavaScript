#!/usr/bin/env python3
"""Run crawl_npm_meta.py under a byte-growth watchdog.

The npm CDN sometimes leaves connections half-open, and on Windows the socket
read timeout does not reliably fire, so a worker can block forever.  This
supervisor restarts the crawler whenever the metadata directory stops growing
for longer than --max-idle-seconds.

Run from the JavaScript repo root:
    python tools/supervise_npm_crawl.py --workers 24 --batch 20000 --log ../../logs/npm_supervisor.log
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


def total_bytes(meta_dir: Path) -> int:
    return sum(p.stat().st_size for p in meta_dir.glob("npm_meta_*.jsonl"))


def repair_parts(meta_dir: Path) -> None:
    """Truncate a partial final JSON line left behind by a killed worker."""
    for part in meta_dir.glob("npm_meta_*.jsonl"):
        with part.open("rb+") as fh:
            fh.seek(0, 2)
            size = fh.tell()
            if size == 0:
                continue
            fh.seek(-1, 2)
            if fh.read(1) == b"\n":
                continue
            pos = size
            chunk_size = 8192
            while pos > 0:
                start = max(0, pos - chunk_size)
                fh.seek(start)
                buf = fh.read(pos - start)
                idx = buf.rfind(b"\n")
                if idx != -1:
                    cut = start + idx + 1
                    if cut < size:
                        fh.truncate(cut)
                    break
                pos = start
            else:
                fh.truncate(0)


def done_batches(state_path: Path, total_batches: int) -> int:
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        return len([x for x in state.get("done", []) if isinstance(x, int)])
    except Exception:
        return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default="tools/cache/npm_current_ids.txt")
    ap.add_argument("--meta-dir", default="tools/cache/npm_meta_parts")
    ap.add_argument("--state", default="tools/cache/npm_meta_state.json")
    ap.add_argument("--seed-cache", default="tools/cache/npm.json")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--batch", type=int, default=20000)
    ap.add_argument("--registry", default="https://registry.npmjs.org")
    ap.add_argument("--max-idle-seconds", type=float, default=270.0)
    ap.add_argument("--poll-seconds", type=float, default=20.0)
    ap.add_argument("--log", default="")
    args = ap.parse_args()

    root = Path.cwd()
    meta_dir = root / args.meta_dir
    state_path = root / args.state
    meta_dir.mkdir(parents=True, exist_ok=True)
    total_ids = sum(1 for _ in (root / args.ids).open(encoding="utf-8", errors="replace"))
    total_batches = (total_ids + args.batch - 1) // args.batch

    log_fh = open(args.log, "a", encoding="utf-8", buffering=1) if args.log else sys.stdout

    def log(line: str) -> None:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {line}", file=log_fh, flush=True)

    crawl_cmd = [
        sys.executable,
        "-u",
        str(root / "tools" / "crawl_npm_meta.py"),
        "--ids",
        str(root / args.ids),
        "--meta-dir",
        str(meta_dir),
        "--state",
        str(state_path),
        "--seed-cache",
        str(root / args.seed_cache),
        "--workers",
        str(args.workers),
        "--batch",
        str(args.batch),
        "--registry",
        args.registry,
    ]
    start = time.time()
    while True:
        repair_parts(meta_dir)
        log(f"starting crawler: {args.workers} workers")
        proc = subprocess.Popen(
            crawl_cmd,
            cwd=str(root),
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        last_size = total_bytes(meta_dir)
        last_change = time.time()
        while proc.poll() is None:
            time.sleep(args.poll_seconds)
            size = total_bytes(meta_dir)
            if size != last_size:
                last_size = size
                last_change = time.time()
            elif time.time() - last_change > args.max_idle_seconds:
                log(
                    f"no growth for {args.max_idle_seconds:.0f}s "
                    f"({last_size / 1e6:.1f} MB), killing pid {proc.pid}"
                )
                proc.kill()
                proc.wait()
                break
            if int(time.time() - start) % (args.poll_seconds * 40) < args.poll_seconds:
                log(
                    f"bytes={last_size / 1e6:.1f} MB "
                    f"batches={done_batches(state_path, total_batches)}/{total_batches}"
                )
        code = proc.returncode
        if code == 0:
            log(
                f"crawler finished: bytes={total_bytes(meta_dir) / 1e6:.1f} MB "
                f"batches={done_batches(state_path, total_batches)}/{total_batches}"
            )
            return 0
        log(f"crawler exited with {code}, restarting")
        time.sleep(3)


if __name__ == "__main__":
    raise SystemExit(main())
