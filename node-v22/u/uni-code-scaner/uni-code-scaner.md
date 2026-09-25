# uni-code-scaner

> 标签: JavaScript

## 简介

>maina.js ``` import codeScaner from "uni-code-scaner" Vue.use(codeScaner) ``` >app.vue ``` this.$startListenScan() ``` >组件内使用，需要注意卸载和隐藏是把监听注销 ``` onShow() {     uni.$on('codeScan', (code) => {       this.getCode(code)     })   }, onUnload() {     console

## 官网

- npm 页面：https://www.npmjs.com/package/uni-code-scaner

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install uni-code-scaner`
- npm registry：https://registry.npmjs.org/uni-code-scaner
