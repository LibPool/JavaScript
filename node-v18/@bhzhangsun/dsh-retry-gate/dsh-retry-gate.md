# @bhzhangsun/dsh-retry-gate

> 标签: 429, admission-control, backpressure, cordis, deepseek, dsh, plugin, rate-limit, retry, rpm, tpm

## 简介

Provider-agnostic admission gate for per-model TPM/RPM limits: paces concurrent sessions instead of letting every one of them collide with a 429. Learns each model's real ceiling from the first 429 it observes, instead of trusting configured assumptions.

## 官网

- 官网：https://github.com/bhzhangsun/awesome-dsh/tree/main/packages/dsh-retry-gate#readme
- 源码仓库：git+https://github.com/bhzhangsun/awesome-dsh.git
- npm 页面：https://www.npmjs.com/package/@bhzhangsun/dsh-retry-gate

## 历史版本号

- 当前版本：0.2.0

- 0.1.0
- 0.2.0

## 获取地址

- npm 安装：`npm install @bhzhangsun/dsh-retry-gate`
- npm registry：https://registry.npmjs.org/@bhzhangsun/dsh-retry-gate
- Node 要求：^22.19.0 || >=24.0.0
