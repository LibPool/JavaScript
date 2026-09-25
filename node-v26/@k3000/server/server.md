# @k3000/server

> 标签: JavaScript

## 简介

tcp、ipc、udp ``` const pools = {     s: {test: 'localhost:9000/test'} } // 9000端 const map = new Map map.set('/test', data => '9000') const s = createServer({port: 9000, map}, pools) // s.close() // 9001端 createServer({port: 9001, listener(path,

## 官网

- npm 页面：https://www.npmjs.com/package/@k3000/server

## 历史版本号

- 当前版本：1.0.9

- 1.0.0
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.7
- 1.0.8
- 1.0.9

## 获取地址

- npm 安装：`npm install @k3000/server`
- npm registry：https://registry.npmjs.org/@k3000/server
