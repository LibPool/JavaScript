# llm-limiter

> 标签: 429, ai, anthropic, concurrency, llm, openai, queue, rate-limit, rate-limiter, retry-after, rpm, throttle, tokens, tpm

## 简介

Token-aware rate limiting for LLM APIs. LLM providers meter requests-per-minute AND tokens-per-minute; generic limiters only count requests. llm-limiter reserves estimated tokens before a call, settles to actual usage after, and queues the rest. Zero depe

## 官网

- 官网：https://github.com/hojoongdev/llm-limiter#readme
- 源码仓库：git+https://github.com/hojoongdev/llm-limiter.git
- npm 页面：https://www.npmjs.com/package/llm-limiter

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install llm-limiter`
- npm registry：https://registry.npmjs.org/llm-limiter
- Node 要求：>=18
