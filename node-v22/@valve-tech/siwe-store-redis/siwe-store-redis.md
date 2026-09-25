# @valve-tech/siwe-store-redis

> 标签: authentication, eip-4361, ethereum, evm, nonce, redis, replay-protection, server, session, siwe, viem

## 简介

Redis-backed SIWE nonce + session stores implementing @valve-tech/siwe-store's async contracts (AsyncNonceStore / AsyncSessionStore). Single-use nonce consume is atomic (Redis DEL), TTLs are enforced server-side by Redis expiry, and sessions are opaque CS

## 官网

- 官网：https://github.com/valve-tech/evm-toolkit/tree/main/packages/siwe-store-redis#readme
- 源码仓库：git+https://github.com/valve-tech/evm-toolkit.git
- npm 页面：https://www.npmjs.com/package/@valve-tech/siwe-store-redis

## 历史版本号

- 当前版本：0.24.1

- 0.22.0
- 0.22.1
- 0.23.0
- 0.24.0
- 0.24.1

## 获取地址

- npm 安装：`npm install @valve-tech/siwe-store-redis`
- npm registry：https://registry.npmjs.org/@valve-tech/siwe-store-redis
- Node 要求：>=20
