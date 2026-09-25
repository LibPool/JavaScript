# @lemon-fe/umi-plugin-mf

> 标签: JavaScript

## 简介

1. module federation的组件尽可能不要有副作用（比如：组件内修改了局部的变量） 2. module federation的入口和umi的入口，即使用了一个相同的模块，模块内部环境不一定是同一个，多个入口之间共享数据不能简单得考虑构造一个局部变量 3. module federation导出的组件，应该与路由无关

## 官网

- npm 页面：https://www.npmjs.com/package/@lemon-fe/umi-plugin-mf

## 历史版本号

- 当前版本：1.1.2

- 1.0.0
- 1.0.0-1
- 1.0.0-2
- 1.0.1
- 1.0.2
- 1.1.0
- 1.1.1
- 1.1.2

## 获取地址

- npm 安装：`npm install @lemon-fe/umi-plugin-mf`
- npm registry：https://registry.npmjs.org/@lemon-fe/umi-plugin-mf
