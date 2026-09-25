# davepi-plugin-sentry

> 标签: davepi, davepi-plugin, error-tracking, monitoring, observability, performance, sentry, tracing

## 简介

Sentry error tracking + performance tracing for dAvePi. Initializes @sentry/node when SENTRY_DSN is set; forwards 5xx errors to Sentry after the framework's errorHandler has produced the response (shape unchanged); auto-tags user.id, accountId, and the fr

## 官网

- 官网：https://docs.davepi.dev/features/plugins/
- 源码仓库：git+https://github.com/projik/davepi.git
- npm 页面：https://www.npmjs.com/package/davepi-plugin-sentry

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install davepi-plugin-sentry`
- npm registry：https://registry.npmjs.org/davepi-plugin-sentry
- Node 要求：>=18
