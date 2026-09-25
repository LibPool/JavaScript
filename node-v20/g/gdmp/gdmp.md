# gdmp

> 标签: JavaScript

## 简介

- 主要将wepy的静态组件，改回小程序原生组件。但部分wepy的特性会被丢弃，例如$broadcast会被丢弃，$emit、$invoke会被强制约束。 - 不再使用脏检查机制，改为Vue的数据响应，无需执行$apply(其实我现在也不知道什么时候才要执行$apply)。 - 数据diff更新，setData的时候只修改改变的值。

## 官网

- npm 页面：https://www.npmjs.com/package/gdmp

## 历史版本号

- 当前版本：1.1.13

- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8
- 1.0.9
- 1.1.0
- 1.1.1
- 1.1.13
- 1.1.2

## 获取地址

- npm 安装：`npm install gdmp`
- npm registry：https://registry.npmjs.org/gdmp
