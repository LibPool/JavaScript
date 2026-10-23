# @argszero/dsh-cancel-cause-guard

> 标签: agent-cancel, agent-lifecycle, cancel-cause, cordis, deepseek-harness, dsh, guard, plugin, session-integrity, turn-end

## 简介

A plugin that keeps one abusive cancellation from making a whole conversation view unreadable. ReactLoopAgent.cancel hands its argument to AbortController.abort(), so it becomes signal.reason; the turn's catch reads it back through abortedCancelCause, who

## 官网

- 官网：https://github.com/argszero/dsh-cancel-cause-guard#readme
- 源码仓库：git+https://github.com/argszero/dsh-cancel-cause-guard.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-cancel-cause-guard

## 历史版本号

- 当前版本：0.2.0

- 0.0.0-stage
- 0.1.0
- 0.2.0

## 获取地址

- npm 安装：`npm install @argszero/dsh-cancel-cause-guard`
- npm registry：https://registry.npmjs.org/@argszero/dsh-cancel-cause-guard
- Node 要求：^22.19 || >=24
