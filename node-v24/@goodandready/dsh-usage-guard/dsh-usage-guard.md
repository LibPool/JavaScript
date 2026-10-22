# @goodandready/dsh-usage-guard

> 标签: deepseek-harness, dsh, dsh-plugin, patch, session-history, token-usage

## 简介

Keeps a malformed token-usage sample from taking a whole session history down with it: a missing or non-numeric counter becomes zero before the harness adds it up, so the fold never yields NaN and already-broken sessions open again.

## 官网

- 官网：https://github.com/GooDAnDReaDY/dsh-usage-guard
- 源码仓库：git+https://github.com/GooDAnDReaDY/dsh-usage-guard.git
- npm 页面：https://www.npmjs.com/package/@goodandready/dsh-usage-guard

## 历史版本号

- 当前版本：0.1.19

- 0.1.15
- 0.1.16
- 0.1.17
- 0.1.18
- 0.1.19
- 0.1.2
- 0.1.3
- 0.1.4
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.9

## 获取地址

- npm 安装：`npm install @goodandready/dsh-usage-guard`
- npm registry：https://registry.npmjs.org/@goodandready/dsh-usage-guard
- Node 要求：>=20
