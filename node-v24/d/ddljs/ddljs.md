# ddljs

> 标签: JavaScript

## 简介

1. 此npm包 可以拿到pg数据库中的表的信息，包括表的结构，字段，索引，注释等，类似于navicat中的DDl。 ## 使用方法 1. npm i ddljs  下载之后，直接require调用即可。例如 const ddljs = require('ddljs'); 例如：const tableinfoTest = ddljs(connectInfo, i.tablename, 1, 1, 1); 2. 此函数一共四个参数(connectInfo, tableName,index,remar

## 官网

- npm 页面：https://www.npmjs.com/package/ddljs

## 历史版本号

- 当前版本：0.1.4

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3
- 0.1.4

## 获取地址

- npm 安装：`npm install ddljs`
- npm registry：https://registry.npmjs.org/ddljs
