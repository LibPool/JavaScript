# abb-component

> 标签: Component, TS, UI, Vue3

## 简介

* 每一个组件实例上挂载install方法 这是为了能够使用 import {LText} from 'abb-component' app.use(LText) 这种方式单独引入组件 ``` import { App } from 'vue' import LShape from './LShape.vue' LShape.install = (app: App) => {   app.component(LShape.name, LShape) }

## 官网

- npm 页面：https://www.npmjs.com/package/abb-component

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install abb-component`
- npm registry：https://registry.npmjs.org/abb-component
