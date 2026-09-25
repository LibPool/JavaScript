# scoped-function

> 标签: compiler, dsl, metaprogramming, utility

## 简介

`ScopedFunction` allows you to inject scope object into `Function` constructor. The properties of the scope object can be accesed in the function body as if they were closure variables: `ScopedFunction('return s;', { s: 'hello' }) -> 'hello'`.

## 官网

- 官网：https://github.com/thoughtspile/scoped-function#readme
- 源码仓库：git+https://github.com/thoughtspile/scoped-function.git
- npm 页面：https://www.npmjs.com/package/scoped-function

## 历史版本号

- 当前版本：0.2.0

- 0.2.0

## 获取地址

- npm 安装：`npm install scoped-function`
- npm registry：https://registry.npmjs.org/scoped-function
