# lock_and_cache

> 标签: cache, lock, redis

## 简介

Most caching libraries don't do locking, meaning that >1 process can be calculating a cached value at the same time. Since you presumably cache things because they cost CPU, database reads, or money, doesn't it make sense to lock while caching?

## 官网

- 官网：https://github.com/faradayio/lock_and_cache_js#readme
- 源码仓库：git+https://github.com/faradayio/lock_and_cache_js.git
- npm 页面：https://www.npmjs.com/package/lock_and_cache

## 历史版本号

- 当前版本：6.0.0-beta.5

- 6.0.0-alpha.2
- 6.0.0-alpha.4
- 6.0.0-alpha.5
- 6.0.0-alpha.6
- 6.0.0-alpha.7
- 6.0.0-alpha.8
- 6.0.0-beta.1
- 6.0.0-beta.2
- 6.0.0-beta.3
- 6.0.0-beta.4
- 6.0.0-beta.5
- 6.0.0-beta.6

## 获取地址

- npm 安装：`npm install lock_and_cache`
- npm registry：https://registry.npmjs.org/lock_and_cache
