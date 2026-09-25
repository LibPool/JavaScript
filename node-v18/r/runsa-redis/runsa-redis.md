# runsa-redis

> 标签: ioredis, keyPrefix, redis

## 简介

* 复用已有ioredis连接,并允许重新指定keyPrefix ```ecmascript 6 //样例代码 let Redis=require('./index'); let redis2 = new Redis({client:ioRedisClient,keyPrefix:'aaa:'}); redis2.get('bbb').then(v=>console.log(v)); //实际key=aaa:bbb

## 官网

- npm 页面：https://www.npmjs.com/package/runsa-redis

## 历史版本号

- 当前版本：1.0.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install runsa-redis`
- npm registry：https://registry.npmjs.org/runsa-redis
