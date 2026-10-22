# @bubuzi/split-asar-builder

> 标签: JavaScript

## 简介

一个用于分隔 asar 文件的构建工具同时支持第三方模块别名 使业务代码与node_modules依赖的代码分离，程序打包后将在输出路径下生成`app.asar`和`deps_x.asar`文件 > `app.asar`为业务代码，`deps_x.asar`为依赖代码,`x`为可变数字，用于区分不同版本的依赖 > 后续计划，当项目依赖更新后通过分多个deps_x.asar文件来减少第三方依赖更新包的大小，避免全量更新

## 官网

- 官网：https://github.com/ybubuzi/split-asar-builder
- 源码仓库：git+https://github.com/ybubuzi/split-asar-builder.git
- npm 页面：https://www.npmjs.com/package/@bubuzi/split-asar-builder

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install @bubuzi/split-asar-builder`
- npm registry：https://registry.npmjs.org/@bubuzi/split-asar-builder
