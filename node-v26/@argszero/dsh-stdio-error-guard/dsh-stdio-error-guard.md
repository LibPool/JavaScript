# @argszero/dsh-stdio-error-guard

> 标签: cordis, deepseek-harness, dsh, econnreset, epipe, plugin, stability, stdio, subprocess, uncaught-exception

## 简介

A containment plugin for the stdio `error` events that kill a dsh host. A Node stream that emits 'error' with no listener throws, and the harness answers an uncaught exception by design with one diagnostic and exit 1 — right for a throw mid-update, wrong

## 官网

- 官网：https://github.com/argszero/dsh-stdio-error-guard#readme
- 源码仓库：git+https://github.com/argszero/dsh-stdio-error-guard.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-stdio-error-guard

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @argszero/dsh-stdio-error-guard`
- npm registry：https://registry.npmjs.org/@argszero/dsh-stdio-error-guard
- Node 要求：^22.19 || >=24
