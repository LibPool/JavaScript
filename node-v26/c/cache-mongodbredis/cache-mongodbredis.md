# cache-mongodbredis

> 标签: JavaScript

## 简介

- 1.使用时需要下载好所需依赖Mongoose（4.11）与Redis（2.8）模块 - 2.直接使用引入在项目中后，实例化对象后传入三个参数,mongose对象，redis连接返回的client的对象，缓存在redis中的存活时间 - 3.之后就可以按照mongoose的原生方式来连接数据库、操作数据库 - 4.调用exec方法后就会为当前调用的方法在redis中添加缓存 ```js const mongoose = require("mongoose"); const redis = require

## 官网

- npm 页面：https://www.npmjs.com/package/cache-mongodbredis

## 历史版本号

- 当前版本：1.0.4

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4

## 获取地址

- npm 安装：`npm install cache-mongodbredis`
- npm registry：https://registry.npmjs.org/cache-mongodbredis
