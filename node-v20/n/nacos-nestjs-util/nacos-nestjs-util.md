# nacos-nestjs-util

> 标签: discovery, nacos, nestjs

## 简介

1.服务注册逻辑：   (1)注册服务时，如果服务器设置了环境变量HOST_IP和SERVER_PORT，那么会把HOST_IP和SERVER_PORT作为服务的IP和PORT进行注册。   (2)如果服务器没有设置环境变量，那么获取.env相关配置(SERVICE_IP,PORT)作为服务的IP和PORT进行注册。   (3)如果本地未配置，那么自动获取服务器IP以及使用默认端口3000进行服务注册。 2.新增获取服务实例集合方法 ## 介绍 本工具基于NestJs8.0以及nacos2.2.1，用于微

## 官网

- 官网：https://github.com/cloudbian/nacos-nestjs-util#readme
- 源码仓库：git+https://github.com/cloudbian/nacos-nestjs-util.git
- npm 页面：https://www.npmjs.com/package/nacos-nestjs-util

## 历史版本号

- 当前版本：1.0.9

- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.7
- 1.0.8
- 1.0.9

## 获取地址

- npm 安装：`npm install nacos-nestjs-util`
- npm registry：https://registry.npmjs.org/nacos-nestjs-util
