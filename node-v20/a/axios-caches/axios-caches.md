# axios-caches

> 标签: JavaScript

## 简介

`axios-caches`是一款基于commonjs的库,用于解决get请求自动缓存的问题, 当设置了 `setConfig(true)`,那么只会执行一次get,第二次会从内存中获取,同样都是自动的,无须写其他代码 当设置了 `setConfig(false)`,那么和axios的get是一样的,每次都会请求实时的数据 ## 方法 axiosCache.get(url, {     ...这里的全部参数和axios保持一致 }) ## 安装 `npm install --save ax

## 官网

- npm 页面：https://www.npmjs.com/package/axios-caches

## 历史版本号

- 当前版本：1.0.4

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4

## 获取地址

- npm 安装：`npm install axios-caches`
- npm registry：https://registry.npmjs.org/axios-caches
