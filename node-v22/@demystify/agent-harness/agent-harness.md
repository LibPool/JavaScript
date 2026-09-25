# @demystify/agent-harness

> 标签: agent, at-least-once, audit, deadline, executor, harness, idempotency, resumable, serverless, workflow

## 简介

The loop that drives an agent-kernel plan to its end, resumably, on a host that can be killed at any moment. At-least-once by design: the cursor advances only on a recorded success, and every step carries a stable `runId:stepId` idempotency key so the hos

## 官网

- 官网：https://github.com/demystify-systems/ai-services-tools/tree/main/packages/agent-harness
- 源码仓库：git+https://github.com/demystify-systems/ai-services-tools.git
- npm 页面：https://www.npmjs.com/package/@demystify/agent-harness

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @demystify/agent-harness`
- npm registry：https://registry.npmjs.org/@demystify/agent-harness
- Node 要求：>=22
