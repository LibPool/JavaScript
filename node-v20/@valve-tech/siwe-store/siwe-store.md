# @valve-tech/siwe-store

> 标签: authentication, eip-4361, ethereum, evm, nonce, replay-protection, server, session, siwe, viem

## 简介

Server-side state for SIWE (Sign-In with Ethereum) that viem/siwe deliberately leaves to the app: a single-use, TTL'd nonce store (atomic consume, delete-before-TTL-check so a race-loser cannot reuse) and an opaque CSPRNG session store bound to an address

## 官网

- 官网：https://github.com/valve-tech/evm-toolkit/tree/main/packages/siwe-store#readme
- 源码仓库：git+https://github.com/valve-tech/evm-toolkit.git
- npm 页面：https://www.npmjs.com/package/@valve-tech/siwe-store

## 历史版本号

- 当前版本：0.24.1

- 0.0.1
- 0.19.0
- 0.20.0
- 0.21.0
- 0.21.0-rc.1
- 0.21.0-rc.2
- 0.22.1
- 0.23.0
- 0.24.0
- 0.24.1

## 获取地址

- npm 安装：`npm install @valve-tech/siwe-store`
- npm registry：https://registry.npmjs.org/@valve-tech/siwe-store
- Node 要求：>=20
