# @koishi-ce/components-shim

> 标签: compat, components, koishi, shim

## 简介

上游包名 @koishijs/components 的下游兼容 shim：供脚手架生成的项目以 npm alias（"@koishijs/components": "npm:@koishi-ce/components-shim@^1.5.22"）钉住该名，把第三方 webui 插件对上游组件库的 dependency 声明指回 @koishi-ce/components，避免 Bun 自动安装拉下 npm 官方组件库形成双实例。版本冻结 1.5.x 线以满足 ^1.5 声明，勿随 changesets b

## 官网

- 官网：https://github.com/Koishi-CE/koishi/tree/main/packages/shim/components-shim
- 源码仓库：git+https://github.com/Koishi-CE/koishi.git
- npm 页面：https://www.npmjs.com/package/@koishi-ce/components-shim

## 历史版本号

- 当前版本：1.5.22

- 1.5.22

## 获取地址

- npm 安装：`npm install @koishi-ce/components-shim`
- npm registry：https://registry.npmjs.org/@koishi-ce/components-shim
