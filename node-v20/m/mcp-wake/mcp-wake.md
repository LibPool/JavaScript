# mcp-wake

> 标签: agent, cli, mcp, model-context-protocol, notification, subscribe, wake

## 简介

Claude Code 对 MCP 协议的支持不够完整：通过 MCP 跑异步长任务（比如指挥 Codex 干活）时，无法订阅服务端的事件，也拿不到任务的最新进展。本项目基于 MCP 标准协议实现了通知订阅，替客户端补足缺口，让 Claude Code 或任意其它客户端都能订阅服务端消息。支持远程 HTTP 与本地 stdio 两种传输。

## 官网

- 官网：https://github.com/OpenSaozi/mcp-wake#readme
- 源码仓库：git+https://github.com/OpenSaozi/mcp-wake.git
- npm 页面：https://www.npmjs.com/package/mcp-wake

## 历史版本号

- 当前版本：0.4.0

- 0.3.0
- 0.4.0

## 获取地址

- npm 安装：`npm install mcp-wake`
- npm registry：https://registry.npmjs.org/mcp-wake
- Node 要求：>=20
