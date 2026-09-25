# hls-easy-admin

> 标签: JavaScript

## 简介

schema中添加linkFunction 传入formModel 可以做一些传参 自行定义跳转还是其他什么操作 ```javascript   linkFunction: ({ formModel }) => {     window.location.href = `https://www.baidu.com?haha=${formModel.aaProjectId}`;   }, ``` ### 高级查询支持 1 定义表格列中新增querySchema属性 用于整合表单的查询条件 按照原search

## 官网

- 源码仓库：git+
- npm 页面：https://www.npmjs.com/package/hls-easy-admin

## 历史版本号

- 当前版本：1.0.5

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5

## 获取地址

- npm 安装：`npm install hls-easy-admin`
- npm registry：https://registry.npmjs.org/hls-easy-admin
- Node 要求：>=16.15.1
