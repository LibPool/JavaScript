# webpack-shimming

> 标签: JavaScript

## 简介

module: {     rules: [        {          test: require.resolve('./src/index.js'),          use: 'imports-loader?thiss=>window,$=jquery'        },        {          test: require.resolve('./src/globals.js'),          use: 'exports-loader?file,parse

## 官网

- npm 页面：https://www.npmjs.com/package/webpack-shimming

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.2

## 获取地址

- npm 安装：`npm install webpack-shimming`
- npm registry：https://registry.npmjs.org/webpack-shimming
