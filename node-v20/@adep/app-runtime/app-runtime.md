# @adep/app-runtime

> 标签: JavaScript

## 简介

AgentDeploy 设备端运行时（M8，APP-003）：离线函数执行器 + 设备端 cloud.db/cloud.storage Provider + 单主 outbox 队列。引擎无关纯 JS——SQLite/文件/原生访问只经注入的桥接口（PRD §3.2.8 硬约束 ④），移动 Capacitor 壳与桌面 Electron 壳共用同一套；CI 用宿主注入的本地 SQLite Provider 跑同一份设备端代码（双态黄金测试的机制来源）。

## 官网

- 官网：https://adep.top
- 源码仓库：git+https://gitcode.com/yunqiang_wu/ai-yunke.git
- npm 页面：https://www.npmjs.com/package/@adep/app-runtime

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @adep/app-runtime`
- npm registry：https://registry.npmjs.org/@adep/app-runtime
