# dsh-wait-guard

> 标签: background, deepseek-harness, dsh, guard, jobs, plugin, timeout

## 简介

Bounded waiting for DeepSeek Harness: caps job_output wait budgets, refuses runaway foreground commands nested in run_code, and explains run_code's own deadline instead of letting it read like a task limit. 让「等」变成有预算的探测，而不是把回合挂住。

## 官网

- npm 页面：https://www.npmjs.com/package/dsh-wait-guard

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-wait-guard`
- npm registry：https://registry.npmjs.org/dsh-wait-guard
- Node 要求：>=22.19.0
