# davepi-plugin-audit

> 标签: audit, audit-log, compliance, davepi, davepi-plugin, events

## 简介

Immutable append-only audit log for dAvePi. Subscribes to the in-process record event bus and writes one row per CRUD mutation (with before/after, JSON-patch diff, actor, IP, user-agent, and request ID) into an auto-registered `audit` collection that's qu

## 官网

- 官网：https://docs.davepi.dev/features/plugins/
- 源码仓库：git+https://github.com/projik/davepi.git
- npm 页面：https://www.npmjs.com/package/davepi-plugin-audit

## 历史版本号

- 当前版本：0.1.2

- 0.1.0
- 0.1.1
- 0.1.2

## 获取地址

- npm 安装：`npm install davepi-plugin-audit`
- npm registry：https://registry.npmjs.org/davepi-plugin-audit
- Node 要求：>=18
