# gql-sql-slicer

> 标签: JavaScript

## 简介

The library is built to query simple dimension/metric based tables. It allows to fetch data in the form you want it. ### example Query: ``` query customers{   fetch(country: US){     plan {       revenue: sum(a: planPrice)     }   } } ``` Response: ``` {

## 官网

- 官网：https://github.com/edjafarov/gql-sql-slicer#readme
- 源码仓库：git+ssh://git@github.com/edjafarov/gql-sql-slicer.git
- npm 页面：https://www.npmjs.com/package/gql-sql-slicer

## 历史版本号

- 当前版本：3.0.0-beta.5

- 3.0.0-alpha.15
- 3.0.0-alpha.4
- 3.0.0-alpha.5
- 3.0.0-alpha.6
- 3.0.0-alpha.7
- 3.0.0-alpha.8
- 3.0.0-alpha.9
- 3.0.0-beta.1
- 3.0.0-beta.2
- 3.0.0-beta.3
- 3.0.0-beta.4
- 3.0.0-beta.5
- 共 80 个版本，完整清单见 npm registry。

## 获取地址

- npm 安装：`npm install gql-sql-slicer`
- npm registry：https://registry.npmjs.org/gql-sql-slicer
