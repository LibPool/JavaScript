# swc-plugin-negative-indices

> 标签: JavaScript

## 简介

A plugin for swc to transform  ```let a = arr[-1];``` to ```let a = arr[arr.length - 1];``` ## Usage ```npm i swc-plugin-negative-indices```   .swcrc ```json {   "jsc": {     "experimental": {       "plugins": [         [           "swc-plugin-negative-in

## 官网

- 官网：https://github.com/RiESAEX/swc-plugin-negative-indices#readme
- 源码仓库：git+https://github.com/RiESAEX/swc-plugin-negative-indices.git
- npm 页面：https://www.npmjs.com/package/swc-plugin-negative-indices

## 历史版本号

- 当前版本：1.1.1

- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8
- 1.1.1

## 获取地址

- npm 安装：`npm install swc-plugin-negative-indices`
- npm registry：https://registry.npmjs.org/swc-plugin-negative-indices
