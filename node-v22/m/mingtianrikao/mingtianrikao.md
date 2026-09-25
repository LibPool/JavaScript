# mingtianrikao

> 标签: JavaScript

## 简介

```js  const fs = require("fs"); const path = require("path"); let str = ""; fs.readdirSync("src").forEach(pathname => {   const realpath = path.join("src",pathname)   if(path.extname(realpath) === ".js"){       str += fs.readFileSync(realpath)

## 官网

- npm 页面：https://www.npmjs.com/package/mingtianrikao

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install mingtianrikao`
- npm registry：https://registry.npmjs.org/mingtianrikao
