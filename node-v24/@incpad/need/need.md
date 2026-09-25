# @incpad/need

> 标签: JavaScript

## 简介

对于普通node程序来说，由于允许随时调用require注入，所以只需要如此： ```$xslt const {need} =require("@incpad/need") const _=need("lodash") _.get({},"xxx") ``` 如果传入第二个参数，即给与指定的上下文，如果第二个参数是个对象， 便会将该库注入到对应的对象中 ```$xslt const {need} =require("@incpad/need") let test={} need("lodash",test

## 官网

- npm 页面：https://www.npmjs.com/package/@incpad/need

## 历史版本号

- 当前版本：1.0.22

- 1.0.21
- 1.0.22

## 获取地址

- npm 安装：`npm install @incpad/need`
- npm registry：https://registry.npmjs.org/@incpad/need
