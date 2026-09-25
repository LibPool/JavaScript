# pg-cancel

> 标签: abort, abortsignal, cancel, connection-pool, node-postgres, pg, postgres, postgresql, statement-timeout, timeout

## 简介

Actually stop a Postgres query when the caller gives up. Aborting a promise does not cancel the backend — it keeps running and keeps the pooled connection. This sends the real cancel request, on its own socket, so it works when the pool is already exhaust

## 官网

- 官网：https://github.com/sparkYJO1/pg-cancel#readme
- 源码仓库：git+https://github.com/sparkYJO1/pg-cancel.git
- npm 页面：https://www.npmjs.com/package/pg-cancel

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install pg-cancel`
- npm registry：https://registry.npmjs.org/pg-cancel
- Node 要求：>=20
