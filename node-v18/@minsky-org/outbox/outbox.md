# @minsky-org/outbox

> 标签: JavaScript

## 简介

Transactional outbox for Postgres (drizzle) plus a BullMQ dispatcher. The job row is written inside the business transaction, so "the state changed" and "the side effect was scheduled" cannot disagree. A relay then claims rows with `FOR UPDATE SKIP LOCKED

## 官网

- npm 页面：https://www.npmjs.com/package/@minsky-org/outbox

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @minsky-org/outbox`
- npm registry：https://registry.npmjs.org/@minsky-org/outbox
