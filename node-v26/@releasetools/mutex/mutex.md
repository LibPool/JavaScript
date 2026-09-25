# @releasetools/mutex

> 标签: JavaScript

## 简介

Advisory locking for CI/CD, backed by a Postgres table. Locks have a TTL and auto-release when the job ends; a GitHub Action and a mutex CLI share the same table, so a lock taken by one blocks the other.

## 官网

- 官网：https://github.com/releasetools/mutex#readme
- 源码仓库：git+https://github.com/releasetools/mutex.git
- npm 页面：https://www.npmjs.com/package/@releasetools/mutex

## 历史版本号

- 当前版本：1.5.0

- 1.3.0
- 1.3.1
- 1.4.0
- 1.5.0

## 获取地址

- npm 安装：`npm install @releasetools/mutex`
- npm registry：https://registry.npmjs.org/@releasetools/mutex
- Node 要求：>=24.0.0
