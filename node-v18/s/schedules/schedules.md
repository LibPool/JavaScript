# schedules

> 标签: JavaScript

## 简介

```js const Scheduler = require('schedules'); const Sch = new Scheduler("MONGO_DB_URI_GOES_HERE"); ;(async() => { await Sch.start(); await Sch.schedule(Date.now() + 5000, { hi: "test" }); console.log(await Sch.findTimestampEnded(Date.now() + 2000))

## 官网

- npm 页面：https://www.npmjs.com/package/schedules

## 历史版本号

- 当前版本：1.0.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install schedules`
- npm registry：https://registry.npmjs.org/schedules
