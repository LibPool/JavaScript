# better-ws

> 标签: JavaScript

## 简介

## 介绍 本项目为基于websocket的二次封装，自定义协议，需与配套的后端一同使用。本工具增加了消息确认机制，通过msg_id与配对的ack进行消息收发的确认，若未收到则一定时间后进行重发。`better-ws`借鉴了axios的拦截器，实现了一系列自己的拦截器，在websocket的通信的生命周期中的恰当位置执行这些拦截器钩子。除此之外还增加了类似http请求的通信方式rpc消息，通过promise封装，发送消息后再`.then`中等待消息结果，或`.catch`中处理发送失败事件。当前版本支持w

## 官网

- 源码仓库：git@gitlab.mrs.ai:bspa/lib/BetterWS.git
- npm 页面：https://www.npmjs.com/package/better-ws

## 历史版本号

- 当前版本：1.0.8

- 0.1.7
- 0.1.8
- 0.1.9
- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8

## 获取地址

- npm 安装：`npm install better-ws`
- npm registry：https://registry.npmjs.org/better-ws
- Node 要求：>=6.0.0
