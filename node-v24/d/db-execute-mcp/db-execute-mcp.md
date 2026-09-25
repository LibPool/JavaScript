# db-execute-mcp

> 标签: ai, controlled-write, database, db-execute, mcp, model-context-protocol, sqlite

## 简介

元数据驱动的 SQLite 受控写库 MCP server（纯 Python 标准库实现，stdio 零依赖）。entity_meta 驱动：intake 把『主体名/指标标签/报告期』等自然语言引用解析为技术键并生成可读计划，confirm 经审计后执行（INSERT/UPDATE/DELETE/UPSERT）；register_entity 免改代码登记任意现有表；内置 calc_system 公式计算引擎与多库切换（DB_PATH）。作为 AI 助手对 SQLite 执行受控增删改的安全通道。

## 官网

- npm 页面：https://www.npmjs.com/package/db-execute-mcp

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.1.0

## 获取地址

- npm 安装：`npm install db-execute-mcp`
- npm registry：https://registry.npmjs.org/db-execute-mcp
- Node 要求：>=14
