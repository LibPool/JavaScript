# win-bridge

> 标签: JavaScript

## 简介

客户端与网站的 window 通信桥 > 调用客户端方法：通过 window.external 调用客户端提供的原生功能； > 暴露网页方法：将网页方法挂载到 window 上，让客户端可以直接调用。 ```vue <!-- src/App.vue --> <script setup lang="ts">   import {useWindowBridgeProvider} from "win-bridge";   import Page from "./page.vue";

## 官网

- npm 页面：https://www.npmjs.com/package/win-bridge

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install win-bridge`
- npm registry：https://registry.npmjs.org/win-bridge
