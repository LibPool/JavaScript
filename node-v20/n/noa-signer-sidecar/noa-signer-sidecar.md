# noa-signer-sidecar

> 标签: ai-agent, governance, hash-chain, key-management, mcp, provenance, receipt, signing

## 简介

Process-isolated Ed25519 signing oracle for noa-receipt: the private key lives ONLY in this separate process, reachable over a Unix domain socket, so a governed proxy (e.g. noa-mcp-proxy) never holds the raw key material in its own process memory.

## 官网

- 官网：https://noatrust.com
- 源码仓库：git+https://github.com/NordenSoft/noa-mandate-core.git
- npm 页面：https://www.npmjs.com/package/noa-signer-sidecar

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.0.1
- 0.1.0

## 获取地址

- npm 安装：`npm install noa-signer-sidecar`
- npm registry：https://registry.npmjs.org/noa-signer-sidecar
- Node 要求：>=20
