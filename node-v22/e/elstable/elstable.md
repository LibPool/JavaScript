# elstable

> 标签: JavaScript

## 简介

<el-s-table :data="tableData"                 :columns="columns"                 border> 传入columns,组件内部循环渲染原element table的每一列 修改了固定列的实现机制，原el-table采用的是多个表格定位实现的，会多渲染表格dom，数据量大电脑性能一般是cpu会达到100%，造成卡顿 参照了ant-design的实现，在同一个表格上使用position: sticky方式实现(对浏览器版

## 官网

- npm 页面：https://www.npmjs.com/package/elstable

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install elstable`
- npm registry：https://registry.npmjs.org/elstable
