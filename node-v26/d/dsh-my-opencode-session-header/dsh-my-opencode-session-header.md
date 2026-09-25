# dsh-my-opencode-session-header

> 标签: JavaScript

## 简介

DSH opencode 会话头注入插件：包装 llm/stream 建立 AsyncLocalStorage 会话上下文 + 单层 globalThis.fetch 补丁，为 opencode.ai（含子域）的推理请求注入 x-opencode-session 头，修复 OpenCode Go 网关 400 MissingSessionID。DSH web plugin: injects the x-opencode-session header for opencode-go model routes

## 官网

- 官网：https://github.com/baosfeng/my-dsh-plugins#readme
- 源码仓库：git+https://github.com/baosfeng/my-dsh-plugins.git
- npm 页面：https://www.npmjs.com/package/dsh-my-opencode-session-header

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-my-opencode-session-header`
- npm registry：https://registry.npmjs.org/dsh-my-opencode-session-header
- Node 要求：>=22
