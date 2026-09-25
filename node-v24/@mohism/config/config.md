# @mohism/config

> 标签: config, mohism

## 简介

- 配置文件使用 `json` 格式  - 配置字段全使用驼峰格式  - 定义了全局配置文件 `global.json` - 运行时配置文件 `local.json`,`production.json` ... 或其他 `{NODE_ENV}.json` - 运行时配置文件 **深层合并** 到 `global.json` - 还能通过环境变量来注入配置 `config_app_appId=1000` 注入到 `config.app.appId`, 依旧是驼峰格式，**下划线代替"."**

## 官网

- npm 页面：https://www.npmjs.com/package/@mohism/config

## 历史版本号

- 当前版本：0.2.3

- 0.0.2
- 0.0.3
- 0.1.0
- 0.2.0
- 0.2.1
- 0.2.2
- 0.2.3

## 获取地址

- npm 安装：`npm install @mohism/config`
- npm registry：https://registry.npmjs.org/@mohism/config
