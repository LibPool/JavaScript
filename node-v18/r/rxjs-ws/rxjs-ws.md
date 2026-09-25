# rxjs-ws

> 标签: JavaScript

## 简介

Ping/Pong example: ```ts const client = new RXSocketClient({ url: 'ws://localhost:3000' }); const pingEvent = client.event('ping'); pingEvent.subscribe((response) => pingEvent.send());

## 官网

- 官网：https://github.com/Luke265/rxjs-ws#readme
- 源码仓库：git+https://github.com/Luke265/rxjs-ws.git
- npm 页面：https://www.npmjs.com/package/rxjs-ws

## 历史版本号

- 当前版本：1.0.6

- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6

## 获取地址

- npm 安装：`npm install rxjs-ws`
- npm registry：https://registry.npmjs.org/rxjs-ws
