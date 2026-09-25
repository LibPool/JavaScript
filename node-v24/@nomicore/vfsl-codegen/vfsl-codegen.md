# @nomicore/vfsl-codegen

> 标签: JavaScript

## 简介

投影生成器（ADR 0005 §3/§4）：吃 `evaluate` 的派生 schema，发射 `VfslPathMap` 增广类型文件。纯发射器——物化折叠/联合分类/判别式检测由求值器完成，本包不做语义再推导。生成物恒以 `import type { PathSchema } from '@nomicore/vfsl-protocol';` 接线协议（任意域，含零别名域——模块性 + 增广目标的恒定保障）。

## 官网

- 官网：https://github.com/nomicore-ai/nomicore
- 源码仓库：git+https://github.com/nomicore-ai/nomicore.git
- npm 页面：https://www.npmjs.com/package/@nomicore/vfsl-codegen

## 历史版本号

- 当前版本：0.3.0

- 0.1.1
- 0.1.2
- 0.1.3
- 0.2.0
- 0.3.0

## 获取地址

- npm 安装：`npm install @nomicore/vfsl-codegen`
- npm registry：https://registry.npmjs.org/@nomicore/vfsl-codegen
