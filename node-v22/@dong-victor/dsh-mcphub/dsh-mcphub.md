# @dong-victor/dsh-mcphub

> 标签: deepseek-harness, dsh, hub, mcp, mcphub, model context protocol, plugin

## 简介

MCPHub 桥接插件（DSH Web GUI）：把本地 MCPHub（http://localhost:3000，@samanhappy/mcphub）聚合暴露的全部 MCP server 工具桥接进 DSH。宿主侧以 MCP Streamable HTTP 客户端连接 MCPHub 聚合端点 /mcp（或 /mcp/<group> 分组端点），把发现到的工具以 mcp__mcphub__<server>-<tool> 形式注册为 agent 原生工具；提供 mcphub_status / mcphub

## 官网

- npm 页面：https://www.npmjs.com/package/@dong-victor/dsh-mcphub

## 历史版本号

- 当前版本：0.2.2

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3
- 0.1.4
- 0.2.1
- 0.2.2

## 获取地址

- npm 安装：`npm install @dong-victor/dsh-mcphub`
- npm registry：https://registry.npmjs.org/@dong-victor/dsh-mcphub
- Node 要求：^22.19.0 || >=24.0.0
