# @unbrowse/undici-shim

> 标签: client, fetch, http, request, shim, unbrowse, undici

## 简介

Drop-in replacement for undici. A safe GET routes through Unbrowse's resolved-route cache ($0 on hit); everything else is native fetch shaped into undici's ResponseData object — same request() returning { statusCode, headers, body } with body.text()/.json

## 官网

- 官网：https://unbrowse.ai/vs/undici
- 源码仓库：git+https://github.com/unbrowse-ai/unbrowse.git
- npm 页面：https://www.npmjs.com/package/@unbrowse/undici-shim

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @unbrowse/undici-shim`
- npm registry：https://registry.npmjs.org/@unbrowse/undici-shim
