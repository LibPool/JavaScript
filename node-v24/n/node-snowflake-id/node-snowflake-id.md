# node-snowflake-id

> 标签: id, node-id, node-snowflake, snowflake, snowflakeid

## 简介

nodejs的分布式id解决方案 参考Twitter的snowflake ```js const SnowflakeID = require("SnowflakeID") const sid = new SnowflakeID() let arr = [] for(let i = 0; i < 10000; i++){     arr.push(sid.generate()) } console.log(arr) ```

## 官网

- 官网：https://github.com/xfy196/SnowflakeID
- 源码仓库：git+https://github.com/xfy196/SnowflakeID.git
- npm 页面：https://www.npmjs.com/package/node-snowflake-id

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install node-snowflake-id`
- npm registry：https://registry.npmjs.org/node-snowflake-id
