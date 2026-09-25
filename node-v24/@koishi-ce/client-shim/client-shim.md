# @koishi-ce/client-shim

> 标签: client, compat, koishi, shim

## 简介

上游包名 @koishijs/client 的下游兼容 shim：供脚手架生成的项目以 npm alias（"@koishijs/client": "npm:@koishi-ce/client-shim@^5.30.11"）钉住该名，把第三方 webui 插件对上游 client 的 peer / dependency 声明指回 @koishi-ce/client，避免 Bun 自动安装拉下 npm 官方 client（连带官方 components 全家桶）形成双实例。版本冻结 5.30.x 线以满足

## 官网

- 官网：https://github.com/Koishi-CE/koishi/tree/main/packages/shim/client-shim
- 源码仓库：git+https://github.com/Koishi-CE/koishi.git
- npm 页面：https://www.npmjs.com/package/@koishi-ce/client-shim

## 历史版本号

- 当前版本：5.30.11

- 5.30.11

## 获取地址

- npm 安装：`npm install @koishi-ce/client-shim`
- npm registry：https://registry.npmjs.org/@koishi-ce/client-shim
