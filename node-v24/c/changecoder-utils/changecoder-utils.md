# changecoder-utils

> 标签: JavaScript

## 简介

判断滚动条到底部，需要用到DOM的三个属性值，即scrollTop、clientHeight、scrollHeight。 1. scrollTop: 滚动条在Y轴上的滚动距离 2. clientHeight: 内容可视区域的高度(元素内容及其边框所占据的空间大小) 3. scrollHeight： 内容可视区域的高度加上溢出（滚动）的距离(元素内容的总高度) 从这三个属性的介绍就可以看出来，滚动条到底部的条件即为scrollTop + clientHeight == scrollHeight。

## 官网

- npm 页面：https://www.npmjs.com/package/changecoder-utils

## 历史版本号

- 当前版本：0.0.3

- 0.0.1
- 0.0.2
- 0.0.3

## 获取地址

- npm 安装：`npm install changecoder-utils`
- npm registry：https://registry.npmjs.org/changecoder-utils
