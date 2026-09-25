# dsh-oc-eof-lenient

> 标签: dsh, eof, finish_reason, llm, middleware, opencode, sse

## 简介

对目标 LLM provider 的模型流做 OpenCode 风格的 EOF 宽容处理：已产出完整内容但以 `TRANSPORT: Stream ended without finish_reason` 结尾的流，按 OpenCode/AI SDK 的语义改写成正常完成（DSH llm/stream 中间件插件）

## 官网

- 官网：https://github.com/xht-code/dsh-oc-eof-lenient#readme
- 源码仓库：git+https://github.com/xht-code/dsh-oc-eof-lenient.git
- npm 页面：https://www.npmjs.com/package/dsh-oc-eof-lenient

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install dsh-oc-eof-lenient`
- npm registry：https://registry.npmjs.org/dsh-oc-eof-lenient
- Node 要求：>=18
