# redis-manager-utils

> 标签: JavaScript

## 简介

### Some main.js ``` const RMU = require( "redis-manager-utils" ); ( async ()=> { 	console.log( "Starting" ); 	var my_con_1 = new RMU( 1 ); 	await my_con_1.init(); 	module.exports.redisConProxy = my_con_1; 	console.log( await my_con_1.exists( "TESTING_KEY

## 官网

- 官网：https://github.com/ceberous/redis-manager#readme
- 源码仓库：git+https://github.com/ceberous/redis-manager.git
- npm 页面：https://www.npmjs.com/package/redis-manager-utils

## 历史版本号

- 当前版本：1.1.8

- 1.0.7
- 1.0.8
- 1.0.9
- 1.1.0
- 1.1.1
- 1.1.2
- 1.1.3
- 1.1.4
- 1.1.5
- 1.1.6
- 1.1.7
- 1.1.8

## 获取地址

- npm 安装：`npm install redis-manager-utils`
- npm registry：https://registry.npmjs.org/redis-manager-utils
