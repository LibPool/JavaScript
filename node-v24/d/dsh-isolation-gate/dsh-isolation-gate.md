# dsh-isolation-gate

> 标签: access-control, agent-safety, ai-agent, authorization, cordis, deepseek-harness, dsh, dsh-bundle, dsh-plugin, isolation, isolation-gate, permissions, sandbox, security, windows

## 简介

门禁 · 目录访问管制（隔离区授权台）：一屏管理「哪些目录受管、各自什么级别」，三级=禁/只读/可读写删；判定同时挂在受管辖通道（bin/gate.mjs）与宿主工具执行门（ctx.tools.guard）上，默认禁、名单缺失一律拒绝（fail-closed）、审计可查、agent 可自查；支持分组批量切、目录选择器与状态文件自动迁移。

## 官网

- 官网：https://github.com/huanlin-labs/dsh-isolation-gate#readme
- 源码仓库：git+https://github.com/huanlin-labs/dsh-isolation-gate.git
- npm 页面：https://www.npmjs.com/package/dsh-isolation-gate

## 历史版本号

- 当前版本：1.0.0

- 0.0.0-stage
- 0.2.0
- 0.2.1
- 0.2.2
- 0.2.3
- 0.3.0
- 0.3.1
- 0.3.2
- 0.4.0
- 1.0.0

## 获取地址

- npm 安装：`npm install dsh-isolation-gate`
- npm registry：https://registry.npmjs.org/dsh-isolation-gate
- Node 要求：>=20.11
