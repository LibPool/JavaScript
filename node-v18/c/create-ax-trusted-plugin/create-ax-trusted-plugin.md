# create-ax-trusted-plugin

> 标签: create-ax-trusted-plugin, plugin, scaffold, vue

## 简介

可信(internal)插件脚手架:一条命令生成一个基于 @ax-npm/host-trusted-sdk-v4 的可信插件骨架(ESM 直出 activate + 自带 Vue + host.ts 指令出口 + 自有能力 token(SSOT) + 共享文案/表单样式/px→vw 适配,dev 裸 vite 原生 sourcemap)。用法:npm create ax-trusted-plugin <id>。生成器本身无机密,公网可装;生成出的工程仍走私有源拉 @ax-npm/* 依赖。

## 官网

- npm 页面：https://www.npmjs.com/package/create-ax-trusted-plugin

## 历史版本号

- 当前版本：1.4.2

- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8
- 1.0.9
- 1.1.1
- 1.2.1
- 1.3.0
- 1.4.0
- 1.4.1
- 1.4.2

## 获取地址

- npm 安装：`npm install create-ax-trusted-plugin`
- npm registry：https://registry.npmjs.org/create-ax-trusted-plugin
- Node 要求：>=18
