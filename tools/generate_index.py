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
from dataclasses import dataclass, field
from pathlib import Path


NPM = "https://registry.npmjs.org"
USER_AGENT = "LibPool-Indexer/1.0 (+https://github.com/LibPool)"
CACHE_PATH = Path(__file__).resolve().parent / "cache" / "npm.json"
NODE_RELEASES = ["node-v18", "node-v20", "node-v22", "node-v24", "node-v26"]


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
    version_lines = "\n".join(f"- {v}" for v in sorted(lib.versions)[-12:] or ["-"])
    if len(lib.versions) > 12:
        version_lines += f"\n- 共 {len(lib.versions)} 个版本，完整清单见 npm registry。"
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


def generate(root: Path, libs: list[JsLib], out_dir: Path) -> dict[str, int]:
    counts = defaultdict(int)
    for lib in libs:
        if not lib.version:
            continue
        text = readme_md(lib)
        for release in node_dirs_for(lib):
            parts = lib.name.split("/")
            target = out_dir / release / Path(*parts)
            target.mkdir(parents=True, exist_ok=True)
            (target / f"{parts[-1]}.md").write_text(text, encoding="utf-8")
            counts[release] += 1
    return dict(counts)


def write_js_readme(root: Path, libs: list[JsLib], counts: dict[str, int]) -> None:
    lines = [
        "# JavaScript / Node.js 库索引",
        "",
        "本目录收录来自 npm registry 的 JavaScript/Node.js 库索引，按 Node 大版本与 npm 包名路径组织：",
        "",
        "- Node 大版本目录：`node-v18`、`node-v20`、`node-v22`、`node-v24`、`node-v26`",
        "- 包路径：`<包名>/<包名>.md`，作用域包如 `@types/node` 位于 `@types/node/node.md`",
        "- 库若兼容多个 Node 大版本，会同时出现在所有后续版本目录中",
        f"- 当前共收录 {len(libs)} 个 npm 包。",
        "",
        "## 数据源",
        "",
        "- npm registry API：https://registry.npmjs.org/<package>",
        "- npm 官网：https://www.npmjs.com/",
        "",
        "## 生成方式",
        "",
        "```bash",
        "python tools/build_seed_list.py",
        "python tools/generate_index.py",
        "```",
        "",
        "按 Node 大版本统计：",
        "",
    ]
    lines += [f"- {k}：{v} 个包" for k, v in counts.items()]
    (root / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="tools/seeds/javascript.json")
    ap.add_argument("--out", default=".")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--refresh-cache", action="store_true")
    args = ap.parse_args()

    root = Path(args.out).resolve()
    libs = load_seeds(Path(args.seeds))
    if args.limit:
        libs = libs[: args.limit]
    cache = load_cache()
    print(f"Processing {len(libs)} packages from {args.seeds}...", flush=True)
    for i, lib in enumerate(libs, 1):
        enrich(lib, cache, use_cache=not args.refresh_cache)
        print(f"  [{i}/{len(libs)}] {lib.name} -> {lib.version or 'failed'}", flush=True)
        time.sleep(0.04)
    save_cache(cache)
    counts = generate(root, libs, root)
    print("Generated:", json.dumps(counts, sort_keys=True), flush=True)
    write_js_readme(root, libs, counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
