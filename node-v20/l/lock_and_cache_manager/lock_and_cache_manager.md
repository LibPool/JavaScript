# lock_and_cache_manager

> 标签: cache, lock, redis, redlock

## 简介

Most caching libraries don't do locking, meaning that >1 process can be calculating a cached value at the same time. Since you presumably cache things because they cost CPU, database reads, or money, doesn't it make sense to lock while caching?

## 官网

- 官网：https://github.com/faradayio/lock_and_cache_js#readme
- 源码仓库：git+https://github.com/faradayio/lock_and_cache_js.git
- npm 页面：https://www.npmjs.com/package/lock_and_cache_manager

## 历史版本号

- 当前版本：5.0.0

- 4.0.1
- 4.2.0
- 4.2.1
- 4.3.0
- 4.5.0
- 4.6.0
- 4.7.0
- 4.8.0
- 5.0.0

## 获取地址

- npm 安装：`npm install lock_and_cache_manager`
- npm registry：https://registry.npmjs.org/lock_and_cache_manager
