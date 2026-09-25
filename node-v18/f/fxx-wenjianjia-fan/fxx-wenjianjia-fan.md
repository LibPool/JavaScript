# fxx-wenjianjia-fan

> 标签: JavaScript

## 简介

这是删除文件和文件夹的方法 ```javascript const fs = require("fs"); const removeDir = (pathdir) => {     //读取文件夹子目录     const arr = fs.readdirSync(pathdir);     arr.forEach(item => {         let middpathdir = pathdir + "/" + item;         let info = fs.statSync

## 官网

- npm 页面：https://www.npmjs.com/package/fxx-wenjianjia-fan

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install fxx-wenjianjia-fan`
- npm registry：https://registry.npmjs.org/fxx-wenjianjia-fan
