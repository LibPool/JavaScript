# @zhushanwen/pi-scheduler

> 标签: pi-package

## 简介

定时任务调度扩展：按 duration（`5m` / `2h` / `1d`）间隔或 cron 表达式，在指定时间向 agent 注入消息。支持一次性提醒（once）与过期策略（expires）。创建入口两路：**人侧 `/schedule` 命令打开创建表单**（表单异步打开，填表时长不受命令通道超时约束），**模型侧 `schedule` tool 直建**（不再弹确认表单；参数不完整时必须先向用户澄清——见「创建方式」）。任务随 owner session 持久化，resume 后继续触发。

## 官网

- npm 页面：https://www.npmjs.com/package/@zhushanwen/pi-scheduler

## 历史版本号

- 当前版本：0.9.1

- 0.4.0
- 0.4.1
- 0.4.2
- 0.4.3
- 0.5.0
- 0.5.1
- 0.5.2
- 0.7.0
- 0.8.0
- 0.8.1
- 0.9.0
- 0.9.1

## 获取地址

- npm 安装：`npm install @zhushanwen/pi-scheduler`
- npm registry：https://registry.npmjs.org/@zhushanwen/pi-scheduler
