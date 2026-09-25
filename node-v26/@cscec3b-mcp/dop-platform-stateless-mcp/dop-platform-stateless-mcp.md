# @cscec3b-mcp/dop-platform-stateless-mcp

> 标签: JavaScript

## 简介

无状态(stateless)版 DOP 平台 MCP,作为 **remote MCP** 供 AI 应用经 dop-ai-gateway → mcp-sandbox 托管调用(三种托管档均支持)。与登录态版 dop-platform-mcp 的区别:**不依赖 @cscec/dop-mcp-tool**(无登录态、无扫码、无切换组织),调用方身份由托管网关注入每条请求的 `params._meta`。

## 官网

- npm 页面：https://www.npmjs.com/package/@cscec3b-mcp/dop-platform-stateless-mcp

## 历史版本号

- 当前版本：0.1.3

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3

## 获取地址

- npm 安装：`npm install @cscec3b-mcp/dop-platform-stateless-mcp`
- npm registry：https://registry.npmjs.org/@cscec3b-mcp/dop-platform-stateless-mcp
- Node 要求：>=20
