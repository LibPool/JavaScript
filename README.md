# JavaScript / Node.js 库索引

本目录收录来自 npm registry 的 JavaScript/Node.js 库索引，按 Node 大版本与 npm 包名路径组织：

- Node 大版本目录：`node-v18`、`node-v20`、`node-v22`、`node-v24`、`node-v26`
- 包路径：`<包名>/<包名>.md`，作用域包如 `@types/node` 位于 `@types/node/node.md`
- 库若兼容多个 Node 大版本，会同时出现在所有后续版本目录中
- 当前共收录 3,978,003 个 npm 包（跨版本约 1,980 万条索引），来源为 npm 复制接口全量包名与 registry 元数据。

## 数据源

- npm 搜索 API：https://registry.npmjs.org/-/v1/search
- npm registry API：https://registry.npmjs.org/<package>
- npm 官网：https://www.npmjs.com/

## 生成方式

```bash
python tools/build_seed_list.py
python tools/crawl_current_ids.py
python tools/crawl_npm_meta.py
python tools/generate_index.py --meta-dir tools/cache/npm_meta_parts --releases node-v18
```

按 Node 大版本统计（索引条目数）：

- node-v18：3,892,858 条
- node-v20：3,943,456 条
- node-v22：3,967,047 条
- node-v24：3,975,300 条
- node-v26：3,976,340 条
