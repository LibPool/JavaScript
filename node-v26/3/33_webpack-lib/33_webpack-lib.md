# 33_webpack-lib

> 标签: JavaScript

## 简介

> 需求： 实现大型正整数相加，打包出开发环境用的js和生产环境用的.min.js。支持amd/cmj/es6/script标签引用等多种方式。 ### 1. 编写加法代码 ``` export default function add(a, b) {   let i = a.length - 1;   let j = b.length - 1;   let carry = 0;   let result = "";   while (i >= 0 || j >= 0) {     let x = 0;

## 官网

- npm 页面：https://www.npmjs.com/package/33_webpack-lib

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install 33_webpack-lib`
- npm registry：https://registry.npmjs.org/33_webpack-lib
