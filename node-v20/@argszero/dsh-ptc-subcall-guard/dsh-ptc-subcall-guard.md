# @argszero/dsh-ptc-subcall-guard

> 标签: cordis, deepseek-harness, dsh, guard, jsonl, plugin, ptc, run_code, session, subCallId

## 简介

Keeps a repeated PTC sub-call id out of the durable session log. deepseek-harness mints a `run_code` sub-call id as `<callId>:ptc:<n>` with `n` counted per execution, so a re-issued tool call numbers from 1 again under the same parent id. The write path a

## 官网

- 官网：https://github.com/argszero/dsh-ptc-subcall-guard#readme
- 源码仓库：git+https://github.com/argszero/dsh-ptc-subcall-guard.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-ptc-subcall-guard

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @argszero/dsh-ptc-subcall-guard`
- npm registry：https://registry.npmjs.org/@argszero/dsh-ptc-subcall-guard
- Node 要求：^22.19 || >=24
