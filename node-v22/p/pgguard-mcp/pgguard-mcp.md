# pgguard-mcp

> 标签: ai-agents, claude, database-security, mcp, model-context-protocol, postgres, postgresql, read-only, rls, supabase, typescript

## 简介

Read-only MCP server for Postgres. A deny-by-default policy file decides which tables and columns an AI agent can see; every query runs inside a BEGIN READ ONLY transaction with a statement timeout, and every decision lands in an audit log.

## 官网

- 官网：https://github.com/Azzaraell/pgguard-mcp#readme
- 源码仓库：git+https://github.com/Azzaraell/pgguard-mcp.git
- npm 页面：https://www.npmjs.com/package/pgguard-mcp

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install pgguard-mcp`
- npm registry：https://registry.npmjs.org/pgguard-mcp
- Node 要求：>=20
