#!/usr/bin/env python3
"""Split npm_meta_parts JSONL rows into one file per first character.

The crawl writes rows in package-id order, so prefix generation can read a
single small file instead of rescanning the whole metadata dump per prefix.

Run from the JavaScript repo root:
    python tools/split_meta_prefixes.py
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta-dir", default="tools/cache/npm_meta_parts")
    ap.add_argument("--out-dir", default="tools/cache/npm_meta_split")
    return ap.parse_args()


def main() -> int:
    args = parse_args()
    src = Path(args.meta_dir)
    dst = Path(args.out_dir)
    dst.mkdir(parents=True, exist_ok=True)
    prefixes = (
        ["-"]
        + [str(i) for i in range(10)]
        + [chr(c) for c in range(ord("A"), ord("Z") + 1)]
        + [chr(c) for c in range(ord("a"), ord("z") + 1)]
        + ["@"]
    )
    handles = {}
    for p in prefixes:
        (dst / p).mkdir(parents=True, exist_ok=True)
        handles[p] = (dst / p / "npm_meta_00.jsonl").open("w", encoding="utf-8", newline="\n")
    counts = {p: 0 for p in prefixes}
    errors = 0
    try:
        for part in sorted(src.glob("npm_meta_*.jsonl")):
            with part.open(encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        row = json.loads(line)
                    except Exception:
                        errors += 1
                        continue
                    name = str(row.get("name") or "")
                    if not name:
                        continue
                    p = name[0]
                    handle = handles.get(p)
                    if handle is None:
                        continue
                    handle.write(line + "\n")
                    counts[p] += 1
        for p in prefixes:
            handles[p].close()
        print("Split counts:", json.dumps(counts, sort_keys=True), flush=True)
        print(f"Total rows: {sum(counts.values()):,}, errors: {errors}", flush=True)
    finally:
        for h in handles.values():
            h.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
