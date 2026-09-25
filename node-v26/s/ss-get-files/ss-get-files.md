# ss-get-files

> 标签: JavaScript

## 简介

const fs = require('fs') const path = require('path') function isFile(path){     return fs.lstatSync(path).isFile() } function isDirectory(path){     return fs.lstatSync(path).isDirectory() } function callback(file, regex, arr) {     let ext = pa

## 官网

- npm 页面：https://www.npmjs.com/package/ss-get-files

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install ss-get-files`
- npm registry：https://registry.npmjs.org/ss-get-files
