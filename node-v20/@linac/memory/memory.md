# @linac/memory

> 标签: JavaScript

## 简介

可以缓存的全局变量，和一般定义变量做缓存不同的是，该库允许任意类型的值作为key值 该库会根据key值生成一个Symbol类型的值作为缓存的实际key 如果传入key值是一个object型的值(typeof key==='object')，会根据构造函数传入的keys做一个pick 如果keys未传或者等于空数组，默认对象的所有属性都参与计算 在需要缓存ajax请求的时候，这个库会非常有用，他可以保证相同的请求参数得到相同的缓存key

## 官网

- npm 页面：https://www.npmjs.com/package/@linac/memory

## 历史版本号

- 当前版本：0.1.0

- 0.0.1-alpha.3
- 0.1.0

## 获取地址

- npm 安装：`npm install @linac/memory`
- npm registry：https://registry.npmjs.org/@linac/memory
