# router-middle

> 标签: JavaScript

## 简介

import {routerMiddle} from 'router-middle' router为new Router()的对象 routerMiddle(router) 然后在页面上写 <script> export default {   name: 'Home1',   middleware:[(routing, next)=>{     console.log("中间件一")     next()   },(routing, next)=>{      console.log("中间件二")

## 官网

- npm 页面：https://www.npmjs.com/package/router-middle

## 历史版本号

- 当前版本：0.0.2

- 0.0.1
- 0.0.2

## 获取地址

- npm 安装：`npm install router-middle`
- npm registry：https://registry.npmjs.org/router-middle
