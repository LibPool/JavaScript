# event-api2

> 标签: JavaScript

## 简介

1. 统一useCapture和options的情况，确认是冒泡还是捕获阶段 ```javascript   let useCapture = false; //默认在冒泡阶段   if(typeof options === 'boolean') {     useCapture = options;   } else if(options instanceof Object && typeof options.capture === 'boolean') {     useCapture = optio

## 官网

- npm 页面：https://www.npmjs.com/package/event-api2

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install event-api2`
- npm registry：https://registry.npmjs.org/event-api2
