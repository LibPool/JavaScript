# ach-conform

> 标签: ach, billing, conformance, linter, payments, stripe, us_bank_account, webhook

## 简介

Static check for the Stripe ACH "succeeded isn't final" trap: webhook handlers that treat payment_intent.succeeded as terminal for us_bank_account charges without also handling the later payment_intent.payment_failed / charge.failed flip.

## 官网

- 官网：https://github.com/fernforge/ach-conform#readme
- 源码仓库：git+https://github.com/fernforge/ach-conform.git
- npm 页面：https://www.npmjs.com/package/ach-conform

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install ach-conform`
- npm registry：https://registry.npmjs.org/ach-conform
- Node 要求：>=18
