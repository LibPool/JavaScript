# @unbrowse/cross-fetch-shim

> 标签: cross-fetch, fetch, http, ponyfill, shim, unbrowse

## 简介

Drop-in replacement for cross-fetch. Keeps the universal fetch ponyfill surface (default fetch + named fetch/Headers/Request/Response) but routes a safe GET through Unbrowse's resolved-route cache ($0 on hit), falling through to native fetch on miss — ide

## 官网

- 官网：https://unbrowse.ai/vs/cross-fetch
- 源码仓库：git+https://github.com/unbrowse-ai/unbrowse.git
- npm 页面：https://www.npmjs.com/package/@unbrowse/cross-fetch-shim

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @unbrowse/cross-fetch-shim`
- npm registry：https://registry.npmjs.org/@unbrowse/cross-fetch-shim
