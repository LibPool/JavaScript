# @ploykit/runtime

> 标签: ploykit, rendering, seo, ssr

## 简介

渲染指令通道的同构契约（框架唯一下沉 JS 的包）：emitDirective 双端实现、routeTable 路由真源、SSR/水合入口工厂。产物为 ESM（相对导入无扩展名，消费方需经 vite/esbuild 等打包器解析）；exports 的 development 条件指向源码，供 monorepo 开发期直出消费；react 系全为 peerDependencies 不打包。

## 官网

- 官网：https://github.com/haozing/ploykit#readme
- 源码仓库：git+https://github.com/haozing/ploykit.git
- npm 页面：https://www.npmjs.com/package/@ploykit/runtime

## 历史版本号

- 当前版本：0.9.0

- 0.4.0
- 0.4.1
- 0.5.0
- 0.6.0
- 0.6.2
- 0.7.0
- 0.7.2
- 0.7.4
- 0.8.0
- 0.8.1
- 0.8.2
- 0.9.0

## 获取地址

- npm 安装：`npm install @ploykit/runtime`
- npm registry：https://registry.npmjs.org/@ploykit/runtime
