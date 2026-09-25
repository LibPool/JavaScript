# as-nodejs-threadpool

> 标签: nodejs-thread-pool, worker_threads

## 简介

基于nodejs worker_threads的线程池。耗时操作或nodejs没有提供异步模式的api（例如解密、同步的文件api）都可以在线程池中执行，业务代码只需要返回一个Promise或async函数给线程池库，至于业务逻辑做什么操作，其实都可以，比如setTimeout，异步操作，async await等

## 官网

- 官网：https://github.com/anysou/nodejs-threadpool#readme
- 源码仓库：git+https://github.com/anysou/nodejs-threadpool.git
- npm 页面：https://www.npmjs.com/package/as-nodejs-threadpool

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install as-nodejs-threadpool`
- npm registry：https://registry.npmjs.org/as-nodejs-threadpool
