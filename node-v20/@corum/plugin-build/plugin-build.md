# @corum/plugin-build

> 标签: JavaScript

## 简介

corum 插件的构建契约唯一载体：宿主半 / 客户端半的 tsdown 配置工厂 + `corum-inline-css` bin。存在的理由是把「每个插件包各抄一份 banner/footer/externals/CSS 内联」收敛成一处 —— 那套闭包工厂契约（__ModuleLoader__ + CJS + externals 白名单 + CSS 内联）写在文档里没人能保证遵守，写在代码里第三方才能复用（插件规范 §7 / 方案 §A.1）。

## 官网

- 官网：https://github.com/kukucaiCndy/Corum-Harness#readme
- 源码仓库：git+https://github.com/kukucaiCndy/Corum-Harness.git
- npm 页面：https://www.npmjs.com/package/@corum/plugin-build

## 历史版本号

- 当前版本：0.6.0

- 0.0.0-stage
- 0.6.0

## 获取地址

- npm 安装：`npm install @corum/plugin-build`
- npm registry：https://registry.npmjs.org/@corum/plugin-build
