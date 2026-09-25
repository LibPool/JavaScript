# @tapnow/nestjs-common

> 标签: JavaScript

## 简介

TapNow-NestJS-Common 的主要目标是为了各个服务聚焦于业务需求，避免各种模块初始化（如Logger，DataBase等）、公用服务等代码重复出现在各个微服务中。TapNow-NestJS-Common 提供一个`CommonModule`来初始化服务需要的模块，提供一些公用的装饰器和Service类来简化业务代码，以提高开发效率，减少维护成本。 `CommonModule` 是一个全局模块，默认会初始化`ConfigModule`, `LoggerModule`（nestjs-pino)

## 官网

- npm 页面：https://www.npmjs.com/package/@tapnow/nestjs-common

## 历史版本号

- 当前版本：1.0.2

- 1.0.2

## 获取地址

- npm 安装：`npm install @tapnow/nestjs-common`
- npm registry：https://registry.npmjs.org/@tapnow/nestjs-common
