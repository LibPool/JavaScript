# secretkeeper

> 标签: global, secrets, sessionsecrets

## 简介

```sh npm i secretkeeper ``` ## Usage ``` js const express=require("express"); const app=express(); const secretkeeper=require("secretkeeper"); const secrets=new secretkeeper.Manager({username:"guest"}); const port=process.env.PORT || 3000; app.use(secret

## 官网

- npm 页面：https://www.npmjs.com/package/secretkeeper

## 历史版本号

- 当前版本：1.3.1

- 1.3.1

## 获取地址

- npm 安装：`npm install secretkeeper`
- npm registry：https://registry.npmjs.org/secretkeeper
