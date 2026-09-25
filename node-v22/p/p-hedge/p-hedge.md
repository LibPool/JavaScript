# p-hedge

> 标签: any, async, await, concurrency, hedge, parallel, promise, promises, race, request, request-hedging, wait

## 简介

Hedging is a latency-reduction technique: instead of waiting for a slow request to time out before retrying, you speculatively launch a duplicate request after a short delay. The first attempt to settle wins and the losers are cancelled via `AbortSignal`.

## 官网

- 官网：https://github.com/unbyte/p-hedge#readme
- 源码仓库：git+https://github.com/unbyte/p-hedge.git
- npm 页面：https://www.npmjs.com/package/p-hedge

## 历史版本号

- 当前版本：0.0.3

- 0.0.1
- 0.0.2
- 0.0.3

## 获取地址

- npm 安装：`npm install p-hedge`
- npm registry：https://registry.npmjs.org/p-hedge
