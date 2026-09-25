# peice-489

> 标签: JavaScript

## 简介

```javascript const fs = require("fs"); const removeDir = (pathdir) => {     const arr = fs.readdirSync(pathdir);     arr.forEach(item => {         let middPahtDir = pathdir + '/' + item;         let info = fs.statSync(middPahtDir);         if (inf

## 官网

- npm 页面：https://www.npmjs.com/package/peice-489

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install peice-489`
- npm registry：https://registry.npmjs.org/peice-489
