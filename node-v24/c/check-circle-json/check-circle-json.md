# check-circle-json

> 标签: JavaScript

## 简介

`npm install check-circle-json` ## usage ```ts const a = {   b: {     c: null   } } as any a.b.c = a const [path1, path2] = getCirclePath(a) console.log(path1, path2) // [ 'b', 'c', 'b' ], [ 'b' ] ``` ```ts const a = {   b: {     c: null   } } console.log

## 官网

- npm 页面：https://www.npmjs.com/package/check-circle-json

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install check-circle-json`
- npm registry：https://registry.npmjs.org/check-circle-json
