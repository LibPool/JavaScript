# l2-send-guard

> 标签: agent, allowlist, eip-7702, ethereum, evm, idempotency, json-rpc, l2, permit2, policy, simulation, viem, wallet

## 简介

Policy guard for agent and bot wallets: checks every signed EVM transaction (allowlists, approve/Permit2 bounds through Multicall3, Safe and 7702 batches, rolling caps, idempotency) and simulates it before your RPC sees it. Never holds keys.

## 官网

- 官网：https://www.yellowgram.dev/oss
- 源码仓库：git+https://github.com/yellowgram/l2-safety-proxy.git
- npm 页面：https://www.npmjs.com/package/l2-send-guard

## 历史版本号

- 当前版本：2.1.0

- 0.5.0
- 1.0.0
- 2.0.0
- 2.1.0

## 获取地址

- npm 安装：`npm install l2-send-guard`
- npm registry：https://registry.npmjs.org/l2-send-guard
- Node 要求：>=20
