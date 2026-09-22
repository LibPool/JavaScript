# JavaScript / Node.js 库索引

本目录收录来自 npm registry 的 JavaScript/Node.js 库索引，按 Node 大版本与 npm 包名路径组织：

- Node 大版本目录：`node-v18`、`node-v20`、`node-v22`、`node-v24`、`node-v26`
- 包路径：`<包名>/<包名>.md`，作用域包如 `@types/node` 位于 `@types/node/node.md`
- 库若兼容多个 Node 大版本，会同时出现在所有后续版本目录中
- 当前共收录 266 个 npm 包。

## 数据源

- npm registry API：https://registry.npmjs.org/<package>
- npm 官网：https://www.npmjs.com/

## 生成方式

```bash
python tools/build_seed_list.py
python tools/generate_index.py
```

按 Node 大版本统计：

- node-v18：242 个包
- node-v20：254 个包
- node-v22：265 个包
- node-v24：265 个包
- node-v26：265 个包