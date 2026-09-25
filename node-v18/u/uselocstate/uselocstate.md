# uselocstate

> 标签: TypeScript, easy, javascript, localStorage, react

## 简介

# 特性 ## 状态持久化 状态分离 存储在localStorage中 ### 原理其实很简单 每个状态其实都是一个useState 只是做了些小改动  ### 状态会有一个副本合集 存在一个js对象中 这个副本只是用来记录 不会导致组件更新 ### 每一次setState 都是改变原有的useState中的数据  ### 每一次读取 如果localStorage中有数据则返回localStorage中的数据 如果没有 则是从副本中读取 ### 基于这一特性 每次父组件更新状态 子组件们都会重新读取loc

## 官网

- 官网：https://github.com/SGDS666/locState
- npm 页面：https://www.npmjs.com/package/uselocstate

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8
- 1.0.9
- 1.1.0

## 获取地址

- npm 安装：`npm install uselocstate`
- npm registry：https://registry.npmjs.org/uselocstate
