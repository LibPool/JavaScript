# untio-hua-tojson

> 标签: JavaScript

## 简介

```javascript   const fs = require('fs');  function toJson(dirName) {      //判断是否为文件      let stat = fs.statSync(dirName);      if (stat.isFile()) {          //是文件          return {              name: dirName,              isFile: true,

## 官网

- npm 页面：https://www.npmjs.com/package/untio-hua-tojson

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install untio-hua-tojson`
- npm registry：https://registry.npmjs.org/untio-hua-tojson
