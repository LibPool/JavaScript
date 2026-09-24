#!/usr/bin/env python3
"""Download the current npm package id list from replicate.npmjs.com.

The changes stream contains every revision ever published.  This script uses
CouchDB `_all_docs` instead, so the saved list contains only ids that still
exist at crawl time.

Run from the repo root:
    python tools/crawl_current_ids.py
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


ENDPOINT = "https://replicate.npmjs.com/registry/_all_docs"
USER_AGENT = "LibPool-Indexer/1.0 (+https://github.com/LibPool)"
OUT = Path(__file__).resolve().parent / "cache" / "npm_current_ids.txt"
STATE = Path(__file__).resolve().parent / "cache" / "npm_current_state.json"


def http_text(url: str, retries: int = 6) -> str:
    last_exc: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=90) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as exc:
            last_exc = exc
            time.sleep(1 + attempt * 2)
    raise RuntimeError(f"failed to fetch {url}: {last_exc}")


def load_state() -> tuple[int, str | None, list[str]]:
    if STATE.exists():
        try:
            data = json.loads(STATE.read_text(encoding="utf-8"))
            return int(data.get("count") or 0), data.get("last_key"), list(data.get("failed", []))
        except Exception:
            pass
    return 0, None, []


def save_state(count: int, last_key: str | None, failed: list[str]) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(
        json.dumps({
            "count": count,
            "last_key": last_key,
            "failed": failed,
            "updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def page_ids(url: str) -> tuple[list[dict], str | None]:
    text = http_text(url)
    data = json.loads(text)
    rows = data.get("rows") or []
    total = int(data.get("total_rows") or 0)
    last_key = data.get("last_key")
    return rows, (last_key if last_key is not None else None), total


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument("--max-pages", type=int, default=0)
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 10000:
        parser.error("--limit must be 1-10000")

    count, last_key, failed = load_state()
    if args.rebuild:
        count = 0
        last_key = None
        failed = []
        OUT.unlink(missing_ok=True)
        STATE.unlink(missing_ok=True)
    mode = "w" if last_key is None else "a"
    out = open(OUT, mode, encoding="utf-8", newline="\n")
    keys_seen: set[str] = set()
    if last_key is not None:
        with OUT.open(encoding="utf-8", errors="replace") as existing:
            for line in existing:
                keys_seen.add(line.strip())
    pages = 0
    print(f"Crawling current npm ids from key={last_key or 'start'}, count={count}", flush=True)

    def fetch_from(start_key: str | None) -> None:
        nonlocal out, count, pages
        current = start_key
        while True:
            params = {"limit": args.limit}
            if current is not None:
                params["startkey"] = json.dumps(current, ensure_ascii=False)
            url = f"{ENDPOINT}?{urllib.parse.urlencode(params)}"
            try:
                rows, _, total = page_ids(url)
            except Exception as exc:
                print(f"  page startkey={current} failed: {exc}", flush=True)
                if current not in failed:
                    failed.append(current)
                break
            if not rows:
                break
            wrote = 0
            for row in rows:
                key = row.get("key") or row.get("id")
                if key is None:
                    continue
                if current is not None and key <= current:
                    continue
                key = str(key)
                if key not in keys_seen:
                    keys_seen.add(key)
                    out.write(key + "\n")
                    wrote += 1
            count += wrote
            pages += 1
            last_row_key = str(rows[-1].get("key") or rows[-1].get("id") or "")
            if len(rows) < args.limit or last_row_key == current:
                current = last_row_key
                break
            current = last_row_key
            if args.max_pages and pages >= args.max_pages:
                break
            time.sleep(0.05)
        return current

    latest = fetch_from(last_key)
    for failed_key in list(failed):
        try:
            latest = fetch_from(failed_key)
            if failed_key in failed:
                failed.remove(failed_key)
        except Exception as exc:
            print(f"retry {failed_key} failed: {exc}", flush=True)

    save_state(count, latest, failed)
    out.close()
    print(f"Done: {count:,} current npm ids; last_key={latest!r}; failed={len(failed)}", flush=True)
    return 0 if not failed else 2


if __name__ == "__main__":
    raise SystemExit(main())
