# @mqschwanda/curry

> 标签: curry, utility

## 简介

```jsx /** * @name curry * @type {Function} * @description recursive autocurry * @since 0.0.1 * @example curry(function, arg1, arg2)(arg3)(arg4, arg5) */ export const curry = (func, array = []) => (...args) => (arr) => ( arr.length === func.length ? func(

## 官网

- 官网：https://github.com/mqschwanda/node-monorepo/tree/master/packages/curry
- 源码仓库：https://github.com/mqschwanda/node-monorepo
- npm 页面：https://www.npmjs.com/package/@mqschwanda/curry

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install @mqschwanda/curry`
- npm registry：https://registry.npmjs.org/@mqschwanda/curry
