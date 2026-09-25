# zy-ttt

> 标签: JavaScript

## 简介

发包的第一天，加油！！！！ ```const fs = require("fs");   const add = (path) => {     let data = fs.readFileSync(path, "utf-8")     console.log("读取当前文件内容" + data)     fs.stat(path, (error, stats) => {         console.log("文件大小" + stats.size)     })

## 官网

- npm 页面：https://www.npmjs.com/package/zy-ttt

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.1.0

## 获取地址

- npm 安装：`npm install zy-ttt`
- npm registry：https://registry.npmjs.org/zy-ttt
