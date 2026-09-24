#!/usr/bin/env python3
"""Download every package id from npm's public CouchDB replicate endpoint.

The registry exposes an ordered changes stream that can be walked with the
since cursor.  This script stores the complete id list in
tools/cache/npm_full_names.txt for later indexing passes.

Run from the repo root:
    python tools/crawl_full_names.py
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


REPLICATE = "https://replicate.npmjs.com/registry"
USER_AGENT = "LibPool-Indexer/1.0 (+https://github.com/LibPool)"
OUT = Path(__file__).resolve().parent / "cache" / "npm_full_names.txt"
STATE = Path(__file__).resolve().parent / "cache" / "npm_full_state.json"


def http_json(url: str, retries: int = 4) -> dict:
    last_exc: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=60) as resp:
                return json.load(resp)
        except Exception as exc:
            last_exc = exc
            time.sleep(1 + attempt * 2)
    raise RuntimeError(f"failed to fetch {url}: {last_exc}")


def load_state() -> tuple[str | None, int]:
    if STATE.exists():
        try:
            data = json.loads(STATE.read_text(encoding="utf-8"))
            return data.get("last_seq"), int(data.get("count") or 0)
        except Exception:
            return None, 0
    return None, 0


def save_state(last_seq: str, count: int) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(
        json.dumps({"last_seq": last_seq, "count": count}, separators=(",", ":")),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10000)
    parser.add_argument("--max-pages", type=int, default=0)
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()

    last_seq, existing_count = load_state()
    if args.rebuild:
        last_seq = None
        existing_count = 0
        OUT.unlink(missing_ok=True)
        STATE.unlink(missing_ok=True)
    mode = "w" if last_seq is None else "a"
    out = open(OUT, mode, encoding="utf-8", newline="\n")
    count = existing_count
    pages = 0
    print(f"Fetching npm registry ids from seq={last_seq or 0}", flush=True)
    while True:
        params = {"limit": args.limit}
        if last_seq:
            params["since"] = last_seq
        url = f"{REPLICATE}/_changes?{urllib.parse.urlencode(params)}"
        data = http_json(url)
        rows = data.get("results") or []
        pages += 1
        for row in rows:
            name = (row.get("id") or "").strip()
            if name:
                out.write(name + "\n")
                count += 1
        next_seq = data.get("last_seq")
        if not next_seq or next_seq == last_seq or not rows:
            break
        last_seq = next_seq
        if count % (args.limit * 20) == 0:
            save_state(last_seq, count)
            print(f"  page {pages}: {count:,} ids, last_seq={last_seq}", flush=True)
        if args.max_pages and pages >= args.max_pages:
            break
        time.sleep(0.05)
    out.close()
    save_state(last_seq, count)
    print(f"Done: {count:,} npm package ids in {pages} pages", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
