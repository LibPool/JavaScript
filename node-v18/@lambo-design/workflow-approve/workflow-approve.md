# @lambo-design/workflow-approve

> 标签: JavaScript

## 简介

- 启动报错找不到docx-preview 修改vue.config.js，在对应属性下增加如下配置。 ```   chainWebpack: (config) => {     config.module       .rule('docx-preview')       .test(/node_modules[\\/]docx-preview[\\/].*\.js$/)       .use('babel')       .loader('babel-loader')       .

## 官网

- npm 页面：https://www.npmjs.com/package/@lambo-design/workflow-approve

## 历史版本号

- 当前版本：1.0.0-beta.148

- 1.0.0-beta.140
- 1.0.0-beta.141
- 1.0.0-beta.142
- 1.0.0-beta.143
- 1.0.0-beta.144
- 1.0.0-beta.145
- 1.0.0-beta.148
- 1.0.0-beta.95
- 1.0.0-beta.96
- 1.0.0-beta.97
- 1.0.0-beta.98
- 1.0.0-beta.99
- 共 139 个版本，完整清单见 npm registry。

## 获取地址

- npm 安装：`npm install @lambo-design/workflow-approve`
- npm registry：https://registry.npmjs.org/@lambo-design/workflow-approve
