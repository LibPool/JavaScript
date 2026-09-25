# node-pa-rpc

> 标签: node, rpc

## 简介

``` const { NodeRpcClient, NodeRpcServer } = require('node-pa-rpc'); const rpcServer = new NodeRpcServer('12200'); const server = rpcServer.createServer((error, paramsData, socket) => {     if (error) {         console.log(error);         return;     }

## 官网

- npm 页面：https://www.npmjs.com/package/node-pa-rpc

## 历史版本号

- 当前版本：1.0.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install node-pa-rpc`
- npm registry：https://registry.npmjs.org/node-pa-rpc
