# @logictan/dsh-loop-guard

> 标签: circuit-breaker, deepseek-harness, dsh, dsh-plugin, guard, output-guard, plugin, reasoning, repetition, thinking-loop

## 简介

Thinking-loop guard for dsh: observes the llm/stream waterfall and breaks a model that degrades into a loop. Detects two per-call shapes (reasoning-only calls, restated-material calls) and re-fires instead of latching; plus two mid-stream breakers that en

## 官网

- 官网：https://github.com/dale0525/dsh-plugins#readme
- 源码仓库：git+https://github.com/dale0525/dsh-plugins.git
- npm 页面：https://www.npmjs.com/package/@logictan/dsh-loop-guard

## 历史版本号

- 当前版本：1.1.4

- 1.0.1
- 1.1.0
- 1.1.1
- 1.1.2
- 1.1.3
- 1.1.4

## 获取地址

- npm 安装：`npm install @logictan/dsh-loop-guard`
- npm registry：https://registry.npmjs.org/@logictan/dsh-loop-guard
