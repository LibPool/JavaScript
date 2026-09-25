# koa2-hold-on

> 标签: await, concurrence, hold, hold on, koa2

## 简介

并发场景下，避免相同耗时操作`action`被重复触发，第`1`个请求触发`action`后，后续`n`个同质请求被`await`住，直到`action`执行结束，`n`个同质请求再继续执行，并直接使用`action`的结果。

## 官网

- npm 页面：https://www.npmjs.com/package/koa2-hold-on

## 历史版本号

- 当前版本：0.1.2

- 0.1.0
- 0.1.1
- 0.1.2

## 获取地址

- npm 安装：`npm install koa2-hold-on`
- npm registry：https://registry.npmjs.org/koa2-hold-on
- Node 要求：>=7.6
