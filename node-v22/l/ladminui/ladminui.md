# ladminui

> 标签: JavaScript

## 简介

在/mock/controller中可添加各控制器代码。 /mock/static.js和/mock/mock-server.js分别实现了脚本ajax拦截响应和mock本地API两套方案，并自动根据运行模式选取方案执行。 1. mock.js在npm run serverless模式下通过拦截替换ajax底层请求，使用脚本模拟服务器响应。该模式下，由于请求是模拟的，在network中不会看到发出请求。 2. 在 num run local模式下，使用devServer托管mock，实现后台响应。该

## 官网

- npm 页面：https://www.npmjs.com/package/ladminui

## 历史版本号

- 当前版本：1.0.1

- 1.0.1

## 获取地址

- npm 安装：`npm install ladminui`
- npm registry：https://registry.npmjs.org/ladminui
