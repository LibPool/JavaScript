# @massapi/jenkins-mcp

> 标签: JavaScript

## 简介

基于 Node.js 的 jenkins MCP 服务，使用 stdio 作为传输层，暴露为 4 个 MCP tools: * list_jobs 获取所有job列表，无输入，输出为name列表 * list_job_build 获取job的构建信息，输入两个参数name和limit，name为job名称, limit默认为5，输出build列表，build中包括number、revision、result、inProgress、timestamp   - result：构建进行中时为 null，完成后为

## 官网

- npm 页面：https://www.npmjs.com/package/@massapi/jenkins-mcp

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install @massapi/jenkins-mcp`
- npm registry：https://registry.npmjs.org/@massapi/jenkins-mcp
- Node 要求：>=20
