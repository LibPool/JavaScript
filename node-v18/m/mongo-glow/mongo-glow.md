# mongo-glow

> 标签: JavaScript

## 简介

```js const uri = //your_database_uri const DB = require("mongo-glow") DB.connect(uri).then(async()=>{     const db = new DB.getDB("test") }) ``` ## usage - set ```js db.set("test",{name:"a"}) ``` - get ```js db.get("test").then(data=>{     console.log(da

## 官网

- npm 页面：https://www.npmjs.com/package/mongo-glow

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.0.1
- 1.0.2
- 1.1.0

## 获取地址

- npm 安装：`npm install mongo-glow`
- npm registry：https://registry.npmjs.org/mongo-glow
