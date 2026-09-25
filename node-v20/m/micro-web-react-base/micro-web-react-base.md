# micro-web-react-base

> 标签: JavaScript

## 简介

- 继承Base应用的组件上下文，所使用的基础依赖比如React，ReactDOM以及组件库都全部来自于Base应用，继承Base应用的组件上下文； - 子组件需要设置微前端配置microConfig中separate为空；这样主应用在加载子应用index config以及main config的时候就不会创建iframe来加载； - 优点是能完全使用Base应用所提供的组件以及工具函数； - 缺点是不可以隔离window全局变量以及样式； - 子应用在main init函数中通过调用setRen

## 官网

- npm 页面：https://www.npmjs.com/package/micro-web-react-base

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install micro-web-react-base`
- npm registry：https://registry.npmjs.org/micro-web-react-base
