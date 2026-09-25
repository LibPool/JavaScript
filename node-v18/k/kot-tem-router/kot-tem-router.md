# kot-tem-router

> 标签: JavaScript

## 简介

```'user strict' module.exports = ({ whiteList }) => {     return async (ctx, next) => {         if (whiteList.includes(ctx.path)) {             await next();             return;         }         try {             const token = ctx.get('token')

## 官网

- npm 页面：https://www.npmjs.com/package/kot-tem-router

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install kot-tem-router`
- npm registry：https://registry.npmjs.org/kot-tem-router
