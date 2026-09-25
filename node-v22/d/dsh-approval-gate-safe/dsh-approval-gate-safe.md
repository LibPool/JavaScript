# dsh-approval-gate-safe

> 标签: approval, auto-approve, cordis, deepseek-harness, dsh, dsh-plugin, sandbox

## 简介

DeepSeek Harness 自动审批门控（兼容加固版）：Flash 模型预判写/命令是否不可回补，安全自动批准、危险转人工（fail-safe），最小人工介入，听人工审查 UI。基于 dsh-approval-gate 0.5.2，修复 DSH 0.1.2-rc.1 API 兼容与插件路由鉴权；0.2.2 补齐 Windows/PowerShell 拒绝词表与路径处理、原子写与配置损坏备份、diff 复杂度、事件/审计日志轮转、CSRF 防线；0.2.3 修复并发丢失更新（审批串行化）、下游异常终态

## 官网

- 源码仓库：https://gitee.com/past-events-sifenruwu/deepseek-harness-electron.git
- npm 页面：https://www.npmjs.com/package/dsh-approval-gate-safe

## 历史版本号

- 当前版本：0.2.3

- 0.2.1
- 0.2.2
- 0.2.3

## 获取地址

- npm 安装：`npm install dsh-approval-gate-safe`
- npm registry：https://registry.npmjs.org/dsh-approval-gate-safe
- Node 要求：>=22
