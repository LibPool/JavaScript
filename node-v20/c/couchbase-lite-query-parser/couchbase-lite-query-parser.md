# couchbase-lite-query-parser

> 标签: JavaScript

## 简介

Query parser to for Couchbase Lite 2 which converts something like ``` SELECT name.first, name.last WHERE grade = 12 AND gpa >= $GPA ``` to ``` ["SELECT", {     "WHAT": [         [".", "name", "first"],         [".", "name", "last"]     ],     "WHERE":

## 官网

- npm 页面：https://www.npmjs.com/package/couchbase-lite-query-parser

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install couchbase-lite-query-parser`
- npm registry：https://registry.npmjs.org/couchbase-lite-query-parser
