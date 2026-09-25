# @workfly/mcp

> 标签: claude, mcp, model-context-protocol, stdio, workbuddy, workfly

## 简介

把 WorkFly 的对外能力以标准 MCP（stdio）暴露给 Claude Code / Claude Desktop / Cursor / WorkBuddy 等 AI 客户端——桥接到本机 loopback 网关。首次调用即弹「连接授权」卡片、令牌自动回灌并本地缓存（零手动复制，连接名自动取客户端自报名），凭授权 token 访问你的研发缺陷 / 文库笔记（token 不含任何后端凭证，能力受授权 scope 约束，写操作再经客户端确认）。

## 官网

- npm 页面：https://www.npmjs.com/package/@workfly/mcp

## 历史版本号

- 当前版本：0.5.0

- 0.1.0
- 0.2.0
- 0.2.1
- 0.2.2
- 0.3.0
- 0.4.0
- 0.4.1
- 0.5.0

## 获取地址

- npm 安装：`npm install @workfly/mcp`
- npm registry：https://registry.npmjs.org/@workfly/mcp
- Node 要求：>=18
