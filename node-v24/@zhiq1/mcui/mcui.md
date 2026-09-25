# @zhiq1/mcui

> 标签: JavaScript

## 简介

1. 使用`vue-cli`创建一个新项目 2. 在src目录下新建packages目录用来放组件代码 3. 在`packages/index.js`中引入所有组件，使用Vue插件形式 ```js // Vue组件要暴露一个有install函数的对象或者暴露一个函数作为install函数 const files = require.context('./components', true) const install = function (Vue) {   files.keys().forEach(ke

## 官网

- npm 页面：https://www.npmjs.com/package/@zhiq1/mcui

## 历史版本号

- 当前版本：0.1.7

- 0.1.1
- 0.1.2
- 0.1.4
- 0.1.5
- 0.1.6
- 0.1.7

## 获取地址

- npm 安装：`npm install @zhiq1/mcui`
- npm registry：https://registry.npmjs.org/@zhiq1/mcui
