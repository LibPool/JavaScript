# dsh-compress-pacing

> 标签: compaction, compress, context, deepseek-harness, dsh, plugin, prompt-cache

## 简介

Paces context compression in DeepSeek Harness: one compress call per window (plus a single cleanup call after a partial rejection), because every compress re-sends the whole context and invalidates the prefix cache. 压缩一次就重发一次上下文，别把压缩拆成一串小调用。

## 官网

- npm 页面：https://www.npmjs.com/package/dsh-compress-pacing

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-compress-pacing`
- npm registry：https://registry.npmjs.org/dsh-compress-pacing
- Node 要求：>=22.19.0
