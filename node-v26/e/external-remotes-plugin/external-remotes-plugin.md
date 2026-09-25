# external-remotes-plugin

> 标签: JavaScript

## 简介

**Host webpack.config** ```js const config = { ...otherConfigs plugins: [ new ModuleFederationPlugin({ name: "app1", remotes: { app2: "app2@[window.app2Url]/remoteEntry.js" } }). new ExternalTemplateRemotesPlugin(), ] } ```

## 官网

- 源码仓库：git@github.com:module-federation/external-remotes-plugin.git
- npm 页面：https://www.npmjs.com/package/external-remotes-plugin

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install external-remotes-plugin`
- npm registry：https://registry.npmjs.org/external-remotes-plugin
