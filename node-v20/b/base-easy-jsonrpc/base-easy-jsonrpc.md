# base-easy-jsonrpc

> 标签: easy-jsonrpc, json, jsonrpc, rpc

## 简介

基于promise封装的jsonrpc库 ## 使用范例 ```         const server = new RpcServer();         server.onNotify("success", (params, router) => {             router.redirect("error");         });         server.onNotify("error", () => {             console.log("notify---

## 官网

- 官网：https://github.com/liuliuabc/easy-jsonrpc#readme
- 源码仓库：git+https://github.com/liuliuabc/easy-jsonrpc.git
- npm 页面：https://www.npmjs.com/package/base-easy-jsonrpc

## 历史版本号

- 当前版本：1.0.7

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7

## 获取地址

- npm 安装：`npm install base-easy-jsonrpc`
- npm registry：https://registry.npmjs.org/base-easy-jsonrpc
