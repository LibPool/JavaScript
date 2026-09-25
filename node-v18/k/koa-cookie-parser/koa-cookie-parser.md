# koa-cookie-parser

> 标签: cookie, koa, middleware, parser

## 简介

## usage ```javascript     const app = new koa();     const CookieParser = require('koa-cookie-parser');     app.use(CookieParser({         cookieNameList:['userId','uuId'],         cipherKey:"hello world",         maxAge:60*60*24     }));

## 官网

- 官网：https://github.com/slashhuang/koa-cookie-parser#readme
- 源码仓库：git+https://github.com/slashhuang/koa-cookie-parser.git
- npm 页面：https://www.npmjs.com/package/koa-cookie-parser

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install koa-cookie-parser`
- npm registry：https://registry.npmjs.org/koa-cookie-parser
