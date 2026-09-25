# @hypelens/hypelens-agent-rail

> 标签: agent, builder, cancel, clawhub, close, hl_place_order, hyperliquid, mcp, model-context-protocol, openclaw, order, perps, place, smithery, trading-agent

## 简介

Mainnet place rail. REQUIRED: hypelens-setup/setup.mjs before start-mcp (start refused without .setup-ok). Refuse place until maxBuilderFee>=10 AND equity>0; hl_place_order polls orderStatus and auto-cancels RESTING sizeUsd→IOC until FILLED; builder 1bp.

## 官网

- 官网：https://github.com/polyparlay/hypelens#readme
- 源码仓库：git+https://github.com/polyparlay/hypelens.git
- npm 页面：https://www.npmjs.com/package/@hypelens/hypelens-agent-rail

## 历史版本号

- 当前版本：0.1.28

- 0.1.23
- 0.1.24
- 0.1.25
- 0.1.26
- 0.1.27
- 0.1.28
- 0.1.4
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.8
- 0.1.9

## 获取地址

- npm 安装：`npm install @hypelens/hypelens-agent-rail`
- npm registry：https://registry.npmjs.org/@hypelens/hypelens-agent-rail
- Node 要求：>=20
