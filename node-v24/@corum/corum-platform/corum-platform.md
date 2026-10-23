# @corum/corum-platform

> 标签: JavaScript

## 简介

平台事实源（corum 核心插件，**不可卸载**）。平台的「行为事实源」只有一个 = 实际运行平台：getPlatform() 返回 process.platform，回答「我现在跑在哪」；getBakedTargetPlatform() 返回打包时烘入的 __CORUM_TARGET_PLATFORM__，回答「这份产物是为谁打的」——后者仅供①运行时一致性断言②host 侧编译期特化瘦身③诊断，**禁止用它做行为决策**（那会让断言退化成恒真废码）。host 侧 cordis 服务（天然跨 bund

## 官网

- 官网：https://github.com/kukucaiCndy/Corum-Harness#readme
- 源码仓库：git+https://github.com/kukucaiCndy/Corum-Harness.git
- npm 页面：https://www.npmjs.com/package/@corum/corum-platform

## 历史版本号

- 当前版本：0.6.0

- 0.0.0-stage
- 0.6.0

## 获取地址

- npm 安装：`npm install @corum/corum-platform`
- npm registry：https://registry.npmjs.org/@corum/corum-platform
