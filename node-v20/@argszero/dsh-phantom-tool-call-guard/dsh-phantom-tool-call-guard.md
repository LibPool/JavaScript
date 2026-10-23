# @argszero/dsh-phantom-tool-call-guard

> 标签: cordis, deepseek-harness, dsh, empty-tool-call-id, guard, llm, llm-stream, phantom-tool-call, plugin, session-poison, stream-guard, tool-call, toolCallId, waterfall

## 简介

An empty-identity tool call can be advertised but never answered: tool/call is admitted with callId "", the harness's own assembler only synthesises a fallback id for a missing one (nullish, so an empty string defeats it), and the paired tool/result is th

## 官网

- 官网：https://github.com/argszero/dsh-phantom-tool-call-guard#readme
- 源码仓库：git+https://github.com/argszero/dsh-phantom-tool-call-guard.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-phantom-tool-call-guard

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @argszero/dsh-phantom-tool-call-guard`
- npm registry：https://registry.npmjs.org/@argszero/dsh-phantom-tool-call-guard
- Node 要求：^22.19 || >=24
