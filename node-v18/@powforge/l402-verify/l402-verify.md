# @powforge/l402-verify

> 标签: agent-payments, bolt11, http-402, l402, lightning, lightning-network, lightning-paywall, lnbits, macaroon, machine-payments, payment-verifier, x402

## 简介

Standalone L402 (Lightning HTTP 402) payment verifier. Zero runtime dependencies. Parses Authorization: L402 <macaroon>:<preimage> headers, verifies the HMAC-signed macaroon, checks sha256(preimage) === payment_hash, and confirms invoice settlement via LN

## 官网

- 官网：https://powforge.dev
- 源码仓库：git+https://github.com/zekebuilds-lab/sats-challenge.git
- npm 页面：https://www.npmjs.com/package/@powforge/l402-verify

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @powforge/l402-verify`
- npm registry：https://registry.npmjs.org/@powforge/l402-verify
- Node 要求：>=18
