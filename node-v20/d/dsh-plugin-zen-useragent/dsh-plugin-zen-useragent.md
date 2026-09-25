# dsh-plugin-zen-useragent

> 标签: deepseek-harness, dsh, opencode, plugin, user-agent, zen

## 简介

让 provider 配置的 headers（如 User-Agent）真正到达 pi-ai 的 API 请求，自动补全 opencode 身份头（ses_/msg_ 会话与请求 ID 格式），并在向 OpenCode Zen 网关发送的请求 body.tools 里补上网关必需的 bash 工具 —— 把请求识别为 opencode 客户端而不是 deepseek-harness，修复 OpenCode ZEN 免费模型 429（FreeUsageLimitError）、400（MissingSessi

## 官网

- 官网：https://github.com/jiujiezongheti/zen-useragent
- 源码仓库：git+https://github.com/jiujiezongheti/zen-useragent.git
- npm 页面：https://www.npmjs.com/package/dsh-plugin-zen-useragent

## 历史版本号

- 当前版本：1.4.0

- 1.0.0
- 1.0.1
- 1.0.2
- 1.1.0
- 1.3.0
- 1.4.0

## 获取地址

- npm 安装：`npm install dsh-plugin-zen-useragent`
- npm registry：https://registry.npmjs.org/dsh-plugin-zen-useragent
- Node 要求：>=18
