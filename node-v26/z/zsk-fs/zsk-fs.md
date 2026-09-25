# zsk-fs

> 标签: JavaScript

## 简介

```js     const fs = require('fs');     fs.readFile('1.txt', 'utf-8', (err, data) => {         if (err) {             console.log('文件读取失败');         } else {             fs.writeFile('2.txt', data + '呵呵呵', 'utf-8', (error) => {                 if (

## 官网

- npm 页面：https://www.npmjs.com/package/zsk-fs

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install zsk-fs`
- npm registry：https://registry.npmjs.org/zsk-fs
