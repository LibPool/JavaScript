# unreadable-typescript

> 标签: type, typescript, unreadable, utility

## 简介

type UnreadableType<T> = T extends object ? { [K in keyof T]: UnreadableType<T[K]> } : T;

## 官网

- 官网：https://github.com/arthur-plazanet/unreadable-typescript#readme
- 源码仓库：git+https://github.com/arthur-plazanet/unreadable-typescript.git
- npm 页面：https://www.npmjs.com/package/unreadable-typescript

## 历史版本号

- 当前版本：1.5.0

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.1.0
- 1.3.0
- 1.4.0
- 1.5.0

## 获取地址

- npm 安装：`npm install unreadable-typescript`
- npm registry：https://registry.npmjs.org/unreadable-typescript
