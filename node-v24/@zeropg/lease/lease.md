# @zeropg/lease

> 标签: distributed-lock, fencing, lease, object-storage

## 简介

Early experiment in the cheapest possible scale-to-zero Postgres. Single-writer lease on object storage for zeropg: conditional-create acquire, CAS renew/takeover, monotonic fencing tokens. No coordination service, no clock dependence for correctness.

## 官网

- 官网：https://github.com/reisepass/zeropg#readme
- 源码仓库：git+https://github.com/reisepass/zeropg.git
- npm 页面：https://www.npmjs.com/package/@zeropg/lease

## 历史版本号

- 当前版本：0.1.0

- 0.0.1
- 0.1.0

## 获取地址

- npm 安装：`npm install @zeropg/lease`
- npm registry：https://registry.npmjs.org/@zeropg/lease
- Node 要求：>=22
