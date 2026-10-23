# @godcreator/gwb-gitea

> 标签: gwb, gwb-plugin

## 简介

gitea HTTP 插件：命令 gitea.http 把 agent 组装好的 API 调用发往配置的 gitea 实例，补上 /api/v1、注入 token、整理回执；命令 gitea.push-mirror.add 用设置里的 GitHub token 开推送镜像，token 不经 agent；调用写法与回执读法写在随包发布的说明书里；别的插件注入服务 gwbGitea，和 gitea.http 走同一个发送函数，另能读出地址、推送地址与 token。

## 官网

- 官网：https://github.com/godcreator02/gwb-gitea#readme
- 源码仓库：git+https://github.com/godcreator02/gwb-gitea.git
- npm 页面：https://www.npmjs.com/package/@godcreator/gwb-gitea

## 历史版本号

- 当前版本：0.1.21

- 0.0.0-stage
- 0.1.19
- 0.1.20
- 0.1.21

## 获取地址

- npm 安装：`npm install @godcreator/gwb-gitea`
- npm registry：https://registry.npmjs.org/@godcreator/gwb-gitea
- Node 要求：>=24
