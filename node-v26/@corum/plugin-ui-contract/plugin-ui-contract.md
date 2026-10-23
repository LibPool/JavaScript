# @corum/plugin-ui-contract

> 标签: JavaScript

## 简介

插件 UI 契约（公开面）：允许第三方插件接触的 UI 面只有两个 —— ①右侧区域覆盖（corum.editor / corum.trajectory / corum.panel，用 slot priority 遮蔽接管）；②设置 ›「扩展」分组里新增自己的设置 section（settings.section list 槽）。**壳布局不可改**：不暴露布局写入面，壳会在发现某区域被插件接管时自动点亮它。第三方只依赖 @corum/plugin-sdk 与本包即可，不需要任何 corum 内部层包。

## 官网

- 官网：https://github.com/kukucaiCndy/Corum-Harness#readme
- 源码仓库：git+https://github.com/kukucaiCndy/Corum-Harness.git
- npm 页面：https://www.npmjs.com/package/@corum/plugin-ui-contract

## 历史版本号

- 当前版本：0.6.0

- 0.0.0-stage
- 0.6.0

## 获取地址

- npm 安装：`npm install @corum/plugin-ui-contract`
- npm registry：https://registry.npmjs.org/@corum/plugin-ui-contract
