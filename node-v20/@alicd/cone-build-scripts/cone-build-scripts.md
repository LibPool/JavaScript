# @alicd/cone-build-scripts

> 标签: JavaScript

## 简介

- ice2 将 webpack 以及相关的依赖封装到了 @builder/pack 里面, 来确保依赖的稳定性 - ice2 底层 hijack 了 require, 来确保 webpack 以及相关的依赖能指向 @builder/pack 里面 - 这样不论在哪里 require webpack/webpack-dev-server, 使用的都是 @builder/pack 的版本 - 所以在调用 start/build/test 之前, 需要确保 hijackWebpack ice2 被调用   -

## 官网

- 源码仓库：git+https://gitlab.alibaba-inc.com/cone-group/cone-build-scripts.git
- npm 页面：https://www.npmjs.com/package/@alicd/cone-build-scripts

## 历史版本号

- 当前版本：0.1.2

- 0.1.0
- 0.1.1
- 0.1.2

## 获取地址

- npm 安装：`npm install @alicd/cone-build-scripts`
- npm registry：https://registry.npmjs.org/@alicd/cone-build-scripts
- Node 要求：>=14.0.0
