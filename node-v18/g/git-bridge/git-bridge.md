# git-bridge

> 标签: JavaScript

## 简介

git-bridge 基于 git，用于管理跨 git repo 的多项目之间的依赖关系。它将项目拆分成 lib（一个 git repo 可以存储多个 lib），通过配置文件，规定 lib 依赖其他哪些 lib。根据定义，lib 可以通过配置项中的脚本生成 dist 文件，这部分文件又能被其他依赖它的 lib 拿到。

## 官网

- 官网：https://github.com/duty-os/git-bridge#readme
- 源码仓库：git+ssh://git@github.com/duty-os/git-bridge.git
- npm 页面：https://www.npmjs.com/package/git-bridge

## 历史版本号

- 当前版本：1.0.20

- 1.0.17
- 1.0.18
- 1.0.19
- 1.0.2
- 1.0.20
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8
- 1.0.9

## 获取地址

- npm 安装：`npm install git-bridge`
- npm registry：https://registry.npmjs.org/git-bridge
