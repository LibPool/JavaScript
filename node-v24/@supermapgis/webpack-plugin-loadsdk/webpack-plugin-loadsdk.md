# @supermapgis/webpack-plugin-loadsdk

> 标签: cesium, clientx, iclient3d, supermap, supermap3d, webpack, webpack-plugin

## 简介

Webpack 插件，用于在 Webpack 项目中集成 @supermapgis/clientx 或 @supermapgis/iclient3d。通过 target 参数切换目标包。提供以下功能：1) 自动设置 window.SUPERMAP3D_BASE_URL（用户无需手动设置）；2) 自动注入 Widget CSS link 标签；3) dev server 静态资源代理（wasm/worker/图片等）；4) 构建后自动复制运行时静态资源到产物目录（支持 glob 过滤）；5) 自动配置 re

## 官网

- npm 页面：https://www.npmjs.com/package/@supermapgis/webpack-plugin-loadsdk

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install @supermapgis/webpack-plugin-loadsdk`
- npm registry：https://registry.npmjs.org/@supermapgis/webpack-plugin-loadsdk
- Node 要求：20 || >=22
