# @koishi-ce/core-shim

> 标签: JavaScript

## 简介

上游包名 @koishijs/core 的下游兼容 shim：供脚手架生成的项目以 npm alias（"@koishijs/core": "npm:@koishi-ce/core-shim@4.18.11"）钉住该名，把 @koishi-ce/loader 精确锁的 peer（4.18.11）指回 @koishi-ce/core，避免 Bun 的 peer 自动安装拉下 npm 官方核心副本。版本冻结 4.18.11（loader 精确 peer，必须逐字相等），勿随 changesets bump。发

## 官网

- npm 页面：https://www.npmjs.com/package/@koishi-ce/core-shim

## 历史版本号

- 当前版本：4.18.11

- 4.18.11

## 获取地址

- npm 安装：`npm install @koishi-ce/core-shim`
- npm registry：https://registry.npmjs.org/@koishi-ce/core-shim
