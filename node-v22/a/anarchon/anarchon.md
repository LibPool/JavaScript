# anarchon

> 标签: cluster, cron, decorators, distributed, interval, jetstream, leaderless, lease, libsql, nats, postgres, postgresql, rabbitmq, redis, scheduler, sqlite, synced-cron, valkey

## 简介

Leaderless cron and interval scheduling for Node.js services, coordinated through your existing datastore. An atomic claim selects one runner per attempt; on Redis, Valkey, PostgreSQL and SQLite a lease lets another instance retry a run whose runner faile

## 官网

- 官网：https://aristoteliss.github.io/anarchon/
- 源码仓库：git+https://github.com/aristoteliss/anarchon.git
- npm 页面：https://www.npmjs.com/package/anarchon

## 历史版本号

- 当前版本：0.4.1

- 0.0.0-stage
- 0.2.0
- 0.3.0
- 0.3.2
- 0.3.3
- 0.4.0
- 0.4.1

## 获取地址

- npm 安装：`npm install anarchon`
- npm registry：https://registry.npmjs.org/anarchon
- Node 要求：>=20
