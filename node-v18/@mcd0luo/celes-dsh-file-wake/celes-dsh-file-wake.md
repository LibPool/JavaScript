# @mcd0luo/celes-dsh-file-wake

> 标签: JavaScript

## 简介

文件级会话唤醒（第二唤醒通道，不依赖桥接 HTTP）：监听 /server-center/runtime/state/session-wake/ 下的唤醒文件（文件名=sessionId），对目标会话 inbox.append + wakeDriver 进程内驱动新一轮处理，处理完将文件移入 done/（追加结果行），会话不可达则移入 failed/。host-only（依赖 schemastery 定义 Config schema）。

## 官网

- npm 页面：https://www.npmjs.com/package/@mcd0luo/celes-dsh-file-wake

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @mcd0luo/celes-dsh-file-wake`
- npm registry：https://registry.npmjs.org/@mcd0luo/celes-dsh-file-wake
