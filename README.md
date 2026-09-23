# JavaScript / Node.js 库索引

本目录收录来自 npm registry 的 JavaScript/Node.js 库索引，按 Node 大版本与 npm 包名路径组织：

- Node 大版本目录：`node-v18`、`node-v20`、`node-v22`、`node-v24`、`node-v26`
- 包路径：`<包名>/<包名>.md`，作用域包如 `@types/node` 位于 `@types/node/node.md`
- 库若兼容多个 Node 大版本，会同时出现在所有后续版本目录中
- 当前共收录 50152 个 npm 包，来源为 npm 搜索 API 全量翻页与人工种子。

## 数据源

- npm 搜索 API：https://registry.npmjs.org/-/v1/search
- npm registry API：https://registry.npmjs.org/<package>
- npm 官网：https://www.npmjs.com/

## 生成方式

```bash
python tools/build_seed_list.py
python tools/generate_index.py --crawl --crawl-limit 50000 --workers 32
```

按 Node 大版本统计：

- node-v18：48093 个包
- node-v20：49092 个包
- node-v22：49788 个包
- node-v24：50030 个包
- node-v26：50074 个包