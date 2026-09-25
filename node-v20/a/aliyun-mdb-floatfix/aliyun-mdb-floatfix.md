# aliyun-mdb-floatfix

> 标签: aliyun, cloud, float, mongodb

## 简介

在云函数中将浮点数存储到mongodb时，数据库会自动转为对象的bug (num字段应该为浮点数类型)： ```javascript {   "_id": "5f44cdd367f1376654bef7a8",   "num": {     "high": 3471712362749231000,     "low": 15648,     "negative": false,     "naN": false,     "infinite": false,     "finite":

## 官网

- npm 页面：https://www.npmjs.com/package/aliyun-mdb-floatfix

## 历史版本号

- 当前版本：1.0.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install aliyun-mdb-floatfix`
- npm registry：https://registry.npmjs.org/aliyun-mdb-floatfix
