# dsh-llm-retry-all

> 标签: deepseek-harness, dsh, dsh-plugin, gateway, llm, retry, settings

## 简介

DSH host plugin: retries EVERY model-gateway error (429, quota, auth, network, ...) with a linear 5s-step backoff capped at 5 minutes, covering agent-loop requests and direct ctx.llm.stream calls (compaction, session title). Max retries configurable in Se

## 官网

- 官网：https://github.com/mimajiushi/dsh-plugins/tree/main/plugins/dsh-llm-retry-all#readme
- 源码仓库：git+https://github.com/mimajiushi/dsh-plugins.git
- npm 页面：https://www.npmjs.com/package/dsh-llm-retry-all

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-llm-retry-all`
- npm registry：https://registry.npmjs.org/dsh-llm-retry-all
