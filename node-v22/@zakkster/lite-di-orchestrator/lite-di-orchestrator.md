# @zakkster/lite-di-orchestrator

> 标签: dependency injection, di, drain, fail-closed, graceful shutdown, kubernetes, liveness, process lifecycle, readiness, self-healing, sigterm, supervision, typescript, zero allocation, zero downtime deploy, zero-gc

## 简介

Graceful-shutdown process-lifecycle capstone for a lite-di service kernel: catch SIGTERM, drain readiness, run an ordered teardown across health + supervisor + container, enforce a hard deadline, and exit with a diagnostic code. Zero deps; opt-in, reversi

## 官网

- 官网：https://github.com/PeshoVurtoleta/lite-di-orchestrator#readme
- 源码仓库：git+https://github.com/PeshoVurtoleta/lite-di-orchestrator.git
- npm 页面：https://www.npmjs.com/package/@zakkster/lite-di-orchestrator

## 历史版本号

- 当前版本：1.0.0

- 1.0.0
- 1.0.0-alpha.1

## 获取地址

- npm 安装：`npm install @zakkster/lite-di-orchestrator`
- npm registry：https://registry.npmjs.org/@zakkster/lite-di-orchestrator
- Node 要求：>=18
