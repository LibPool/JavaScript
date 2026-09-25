# project-send-accept

> 标签: JavaScript

## 简介

1. 客户端发送连接请求 2. 服务端接收连接请求，并发送连接响应 3. 客户端接收连接响应，并发送连接确认 4. 服务端接收连接确认，生成公钥和私钥，并发送公钥给客户端 5. 客户端接收公钥，生成公钥和私钥，并发送公钥给服务端 6. 服务端接收公钥，并使用对方公钥加密生成一段随机数据，并发送给客户端 7. 客户端接收随机数据，使用私钥解密，同时用对方公钥加密此数据，并发送给服务端 8. 服务端接收加密数据，使用私钥解密，并发送确认消息（此步骤及之后都使用加密数据）给客户端 9. 客户端接

## 官网

- npm 页面：https://www.npmjs.com/package/project-send-accept

## 历史版本号

- 当前版本：2.0.0-alpha.4

- 1.0.5
- 1.0.6
- 1.0.7
- 2.0.0-alpha.1
- 2.0.0-alpha.2
- 2.0.0-alpha.3
- 2.0.0-alpha.4

## 获取地址

- npm 安装：`npm install project-send-accept`
- npm registry：https://registry.npmjs.org/project-send-accept
- Node 要求：>=12
