# sf-nest-trace

> 标签: JavaScript

## 简介

## 配置使trace生效 在src目录创建trace.ts ```typescript const traceConfig = config().trace // @ts-ignore initTracingWithProvider({   ...traceConfig,   ignoreIncomingRequestHook: (request) => {   const urls = [     '/deploy/ready',     '/deploy/live',   ]   for (cons

## 官网

- npm 页面：https://www.npmjs.com/package/sf-nest-trace

## 历史版本号

- 当前版本：0.1.10

- 0.0.7
- 0.0.9
- 0.1.0
- 0.1.1
- 0.1.10
- 0.1.2
- 0.1.3
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.8
- 0.1.9

## 获取地址

- npm 安装：`npm install sf-nest-trace`
- npm registry：https://registry.npmjs.org/sf-nest-trace
