# um-share-core

> 标签: JavaScript

## 简介

友盟H5端的分享追踪 ## 设计思路 采用核心包+插件方式 - 核心包提供一个方法，该方法按照协议上报到友盟分享统计链路,实现时遵循兼容性优先原则, 能独立运行,并适当对外插件暴露必要的设置方法和生命周期事件。 - 插件可以监听核心包事件，并能够调用核心包的统计链路，能够设置核心包提供的公共属性

## 官网

- 源码仓库：http://gitlab.alibaba-inc.com/jssdk/share.git
- npm 页面：https://www.npmjs.com/package/um-share-core

## 历史版本号

- 当前版本：1.2.5

- 1.1.2
- 1.1.3
- 1.1.6
- 1.1.7
- 1.1.8
- 1.1.9
- 1.2.0
- 1.2.1
- 1.2.2
- 1.2.3
- 1.2.4
- 1.2.5

## 获取地址

- npm 安装：`npm install um-share-core`
- npm registry：https://registry.npmjs.org/um-share-core
