# fh-public

> 标签: JavaScript

## 简介

- 打包时需要配置extend把vue，element+，以及依赖主项目的@/common等资源的路径给忽略掉（还有useMainStore,lodash,axios）； - 打包时还是使用本身的自动导入功能来导入vue，lodash，axios的相关变量，以及element+的组件；   // 上一条是因为主应用的自动导入无法包含/node-modules里的文件（vite5不行，之前vite3的好像可以？） - element+的样式始终使用主应用的（主应用的是全量导入）；

## 官网

- npm 页面：https://www.npmjs.com/package/fh-public

## 历史版本号

- 当前版本：0.0.5

- 0.0.1
- 0.0.2
- 0.0.3
- 0.0.4
- 0.0.5

## 获取地址

- npm 安装：`npm install fh-public`
- npm registry：https://registry.npmjs.org/fh-public
