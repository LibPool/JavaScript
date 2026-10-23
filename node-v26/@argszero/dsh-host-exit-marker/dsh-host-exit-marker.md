# @argszero/dsh-host-exit-marker

> 标签: cordis, crash, deepseek-harness, diagnostics, dsh, host, observability, plugin, process, sighup, signal, sigterm

## 简介

Leave a record when a dsh host process dies. Discussion #10022 reports that from the outside a crash, a quit and a silent SIGTERM are indistinguishable: the desktop shell kills the host with SIGTERM (apps/desktop/src/host-process.ts:209, :296), profile-bo

## 官网

- 官网：https://github.com/argszero/dsh-host-exit-marker#readme
- 源码仓库：git+https://github.com/argszero/dsh-host-exit-marker.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-host-exit-marker

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @argszero/dsh-host-exit-marker`
- npm registry：https://registry.npmjs.org/@argszero/dsh-host-exit-marker
- Node 要求：^22.19 || >=24
