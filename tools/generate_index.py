#!/usr/bin/env python3
"""Generate the LibPool JavaScript/Node.js library index from npm metadata.

Layout:
  node-v<major>/<package-name>/<package-name>.md

Run from the repo root:
    python tools/generate_index.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path


NPM = "https://registry.npmjs.org"
USER_AGENT = "LibPool-Indexer/1.0 (+https://github.com/LibPool)"
CACHE_PATH = Path(__file__).resolve().parent / "cache" / "npm.json"
NODE_RELEASES = ["node-v18", "node-v20", "node-v22", "node-v24", "node-v26"]

CRAWL_QUERIES = [
    "javascript", "node", "react", "vue", "angular", "typescript", "css", "html",
    "http", "web", "api", "cli", "test", "ui", "database", "sql", "orm",
    "auth", "security", "parser", "server", "tool", "util", "helper", "async",
    "stream", "state", "router", "template", "plugin", "component", "chart",
    "editor", "animation", "network", "socket", "queue", "cache", "logger",
    "config", "validation", "schema", "data", "json", "markdown", "image",
    "pdf", "excel", "crypto", "http-client", "react-native", "webpack", "vite",
    "babel", "eslint", "jest", "storybook", "tailwind", "three", "game",
    "visualization", "form", "table", "router-dom", "animation-dom",
]


@dataclass
class JsLib:
    name: str
    tags: list[str] = field(default_factory=list)
    version: str = ""
    description: str = ""
    homepage: str = ""
    repository: str = ""
    engines_node: str = ""
    versions: list[str] = field(default_factory=list)
    version_count: int = 0

    @property
    def safe_name(self) -> str:
        return re.sub(r"[^A-Za-z0-9._@+-]", "-", self.name)


def http_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def load_seeds(path: Path) -> list[JsLib]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [JsLib(name=item["name"], tags=item.get("tags", [])) for item in data]


def load_meta_dir(path: Path, prefix: str = "") -> list[JsLib]:
    """Load the lean metadata dump produced by crawl_npm_meta.py."""
    libs: list[JsLib] = []
    errors = 0
    for part in sorted(path.glob("npm_meta_*.jsonl")):
        with part.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                if prefix and not line.startswith('{"name":"' + prefix):
                    continue
                try:
                    item = json.loads(line)
                except Exception:
                    errors += 1
                    continue
                name = item.get("name") or ""
                if prefix and not name.startswith(prefix):
                    continue
                libs.append(
                    JsLib(
                        name=name,
                        tags=item.get("tags") or [],
                        version=item.get("version") or "",
                        description=item.get("description") or "",
                        homepage=item.get("homepage") or "",
                        repository=item.get("repository") or "",
                        engines_node=item.get("engines_node") or "",
                        versions=item.get("versions") or [],
                        version_count=int(item.get("version_count") or 0),
                    )
                )
    if errors:
        print(f"  {errors:,} unreadable meta lines skipped", flush=True)
    return [lib for lib in libs if lib.name]


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(data: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def crawl_npm_search(limit: int) -> list[JsLib]:
    """Collect distinct npm packages via the public search API."""
    found: dict[str, JsLib] = {}
    for q in CRAWL_QUERIES:
        for start in range(0, 10001, 250):
            url = f"{NPM}/-/v1/search?text={urllib.parse.quote(q)}&size=250&from={start}"
            try:
                data = http_json(url)
            except Exception:
                break
            objects = data.get("objects") or []
            if not objects:
                break
            for obj in objects:
                pkg = obj.get("package") or {}
                name = (pkg.get("name") or "").strip()
                if not name:
                    continue
                if name not in found:
                    found[name] = JsLib(name=name)
                if len(found) >= limit:
                    return list(found.values())
            print(f"  query={q} from={start} collected={len(found)}", flush=True)
            time.sleep(0.08)
    return list(found.values())


def node_major_baseline(engine_range: str) -> int | None:
    """Pick the minimum supported Node major from an engines.node expression."""
    if not engine_range:
        return None
    numbers: list[int] = []
    for m in re.finditer(r"(?:>=|>|~|\^)?\s*v?(\d+)", engine_range):
        prefix = (m.group(0) or "").strip()
        if prefix.startswith("<") or prefix.startswith("<="):
            continue
        numbers.append(int(m.group(1)))
    return min(numbers) if numbers else None


def node_dirs_for(lib: JsLib) -> list[str]:
    baseline = node_major_baseline(lib.engines_node)
    if baseline is None:
        baseline = 18
    return [d for d in NODE_RELEASES if int(d.replace("node-v", "")) >= baseline]


def enrich(lib: JsLib, cache: dict, use_cache: bool) -> None:
    key = lib.name
    if use_cache and key in cache:
        entry = cache[key]
        for attr in ("version", "description", "homepage", "repository", "engines_node", "versions"):
            setattr(lib, attr, entry.get(attr, ""))
        lib.tags = list(dict.fromkeys(lib.tags + entry.get("tags", [])))
        return

    try:
        data = http_json(f"{NPM}/{urllib.parse.quote(lib.name, safe='')}")
    except Exception as exc:
        print(f"  {lib.name}: fetch failed -> {exc}", flush=True)
        return
    lib.name = data.get("name") or lib.name
    dist_tags = data.get("dist-tags") or {}
    lib.version = dist_tags.get("latest") or ""
    versions = data.get("versions") or {}
    lib.versions = list(versions.keys())
    if lib.version and lib.version in versions:
        meta = versions[lib.version]
    else:
        meta = versions.get(lib.versions[0]) if lib.versions else {}
    lib.description = (meta.get("description") or "").strip()
    lib.homepage = (meta.get("homepage") or "").strip()
    repo = meta.get("repository")
    if isinstance(repo, dict):
        lib.repository = (repo.get("url") or "").strip()
    elif isinstance(repo, str):
        lib.repository = repo.strip()
    engines = meta.get("engines") or {}
    if isinstance(engines, dict):
        lib.engines_node = (engines.get("node") or "").strip()
    elif isinstance(engines, list):
        node_ranges = [str(e) for e in engines if "node" in str(e).lower()]
        lib.engines_node = ", ".join(node_ranges) or ", ".join(str(e) for e in engines)
    elif isinstance(engines, str):
        lib.engines_node = engines.strip()
    if not lib.homepage:
        lib.homepage = f"https://www.npmjs.com/package/{urllib.parse.quote(lib.name, safe='@/')}"
    cache[key] = {
        "name": lib.name,
        "version": lib.version,
        "description": lib.description,
        "homepage": lib.homepage,
        "repository": lib.repository,
        "engines_node": lib.engines_node,
        "versions": lib.versions,
        "tags": lib.tags,
    }


def readme_md(lib: JsLib) -> str:
    total_versions = lib.version_count or len(lib.versions)
    version_lines = "\n".join(f"- {v}" for v in sorted(lib.versions)[-12:] or ["-"])
    if total_versions > len(lib.versions):
        version_lines += f"\n- 共 {total_versions:,} 个版本，完整清单见 npm registry。"
    websites = []
    if lib.homepage:
        websites.append(f"- 官网：{lib.homepage}")
    if lib.repository:
        websites.append(f"- 源码仓库：{lib.repository}")
    websites.append(f"- npm 页面：https://www.npmjs.com/package/{urllib.parse.quote(lib.name, safe='@/')}")
    downloads = [
        f"- npm 安装：`npm install {lib.name}`",
        f"- npm registry：https://registry.npmjs.org/{urllib.parse.quote(lib.name, safe='@/')}",
    ]
    if lib.engines_node:
        downloads.append(f"- Node 要求：{lib.engines_node}")
    tags = ", ".join(sorted(set(lib.tags))) if lib.tags else "JavaScript"
    desc = lib.description or f"{lib.name} - JavaScript library from npm"
    return f"""# {lib.name}

> 标签: {tags}

## 简介

{desc}

## 官网

{chr(10).join(websites)}

## 历史版本号

- 当前版本：{lib.version or "未知"}

{version_lines}

## 获取地址

{chr(10).join(downloads)}
"""


def generate(root: Path, libs: list[JsLib], out_dir: Path, releases: list[str] | None = None) -> dict[str, int]:
    counts = defaultdict(int)
    targets = releases or NODE_RELEASES
    for lib in libs:
        if not lib.version:
            continue
        text = readme_md(lib)
        for release in node_dirs_for(lib):
            if release not in targets:
                continue
            parts = lib.name.split("/")
            target = out_dir / release / Path(*parts)
            target.mkdir(parents=True, exist_ok=True)
            md_path = target / f"{parts[-1]}.md"
            if md_path.exists():
                continue
            md_path.write_text(text, encoding="utf-8")
            counts[release] += 1
    return dict(counts)


def load_existing_counts(root: Path) -> dict[str, int]:
    readme = root / "README.md"
    if not readme.exists():
        return {}
    counts: dict[str, int] = {}
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\- (node-v\d+)[:：]\s+([\d,]+) 个包", line)
        if match:
            counts[match.group(1)] = int(match.group(2).replace(",", ""))
    return counts


def load_existing_total(root: Path) -> int:
    counts = load_existing_counts(root)
    if counts.get("node-v26"):
        return counts["node-v26"]
    readme = root / "README.md"
    if not readme.exists():
        return 0
    for line in readme.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\- 当前共收录 ([\d,]+) 个 npm 包", line)
        if match:
            return int(match.group(1).replace(",", ""))
    return 0


def write_js_readme(root: Path, total: int, counts: dict[str, int], releases: list[str] | None) -> None:
    merged = load_existing_counts(root)
    for release, count in counts.items():
        merged[release] = merged.get(release, 0) + count
    total_all = load_existing_total(root) + total
    lines = [
        "# JavaScript / Node.js 库索引",
        "",
        "本目录收录来自 npm registry 的 JavaScript/Node.js 库索引，按 Node 大版本与 npm 包名路径组织：",
        "",
        "- Node 大版本目录：`node-v18`、`node-v20`、`node-v22`、`node-v24`、`node-v26`",
        "- 包路径：`<包名>/<包名>.md`，作用域包如 `@types/node` 位于 `@types/node/node.md`",
        "- 库若兼容多个 Node 大版本，会同时出现在所有后续版本目录中",
        f"- 当前共收录 {total_all:,} 个 npm 包，来源为 npm 复制接口全量包名与 registry 元数据。",
        "",
        "## 数据源",
        "",
        "- npm 搜索 API：https://registry.npmjs.org/-/v1/search",
        "- npm registry API：https://registry.npmjs.org/<package>",
        "- npm 官网：https://www.npmjs.com/",
        "",
        "## 生成方式",
        "",
        "```bash",
        "python tools/build_seed_list.py",
        "python tools/crawl_current_ids.py",
        "python tools/crawl_npm_meta.py",
        "python tools/generate_index.py --meta-dir tools/cache/npm_meta_parts --releases node-v18",
        "```",
        "",
        "按 Node 大版本统计：",
        "",
    ]
    lines += [f"- {k}：{v:,} 个包" for k, v in merged.items()]
    (root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="tools/seeds/javascript.json")
    ap.add_argument("--out", default=".")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--crawl", action="store_true", help="crawl npm search API and merge into seeds")
    ap.add_argument("--crawl-limit", type=int, default=50000, help="max packages to collect from search")
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--refresh-cache", action="store_true")
    ap.add_argument("--meta-dir", default="", help="read all metadata from crawl_npm_meta.py JSONL parts")
    ap.add_argument("--prefix", default="", help="only process package names starting with this prefix")
    ap.add_argument("--releases", default="", help="comma-separated node-vXX directories to write")
    args = ap.parse_args()

    root = Path(args.out).resolve()
    releases = [r.strip() for r in args.releases.split(",") if r.strip()] if args.releases else None
    if args.meta_dir:
        meta_dir = Path(args.meta_dir)
        libs = load_meta_dir(meta_dir, args.prefix)
        print(f"Loaded {len(libs):,} packages from {meta_dir}", flush=True)
    else:
        libs = load_seeds(Path(args.seeds))
        if args.crawl:
            crawled = crawl_npm_search(args.crawl_limit)
            existing = {lib.name for lib in libs}
            added = 0
            for lib in crawled:
                if lib.name not in existing:
                    libs.append(lib)
                    existing.add(lib.name)
                    added += 1
            print(f"Crawled {len(crawled)} names from npm search, added {added} new packages", flush=True)
    if args.prefix:
        libs = [lib for lib in libs if lib.name.startswith(args.prefix)]
        print(f"Prefix {args.prefix!r}: {len(libs):,} packages", flush=True)
    if args.limit:
        libs = libs[: args.limit]
    if not args.meta_dir:
        cache = load_cache()
        print(f"Processing {len(libs)} packages from {args.seeds}...", flush=True)
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futures = [ex.submit(enrich, lib, cache, not args.refresh_cache) for lib in libs]
            for i, fut in enumerate(as_completed(futures), 1):
                try:
                    fut.result()
                except Exception as exc:
                    print(f"  enrich error -> {exc}", flush=True)
                if i % 500 == 0 or i == len(futures):
                    save_cache(cache)
                    print(f"  enriched {i}/{len(futures)}", flush=True)
        save_cache(cache)
    counts = generate(root, libs, root, releases)
    print("Generated:", json.dumps(counts, sort_keys=True), flush=True)
    write_js_readme(root, len(libs), counts, releases)
    return 0


if __name__ == "__main__":
    sys.exit(main())
