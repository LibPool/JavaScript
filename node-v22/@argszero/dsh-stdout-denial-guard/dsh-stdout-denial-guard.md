# @argszero/dsh-stdout-denial-guard

> 标签: bwrap, cordis, deepseek-harness, denial, diagnostics, dsh, escalation, landlock, plugin, sandbox, seatbelt, stdout

## 简介

Classifies sandbox denials the harness reports on stdout. The harness matches each runner's denial dialect against stderr only, so a program that prints its failing path on stdout - or any command that merged the streams with 2>&1 - exits non-zero with no

## 官网

- 官网：https://github.com/argszero/dsh-stdout-denial-guard#readme
- 源码仓库：git+https://github.com/argszero/dsh-stdout-denial-guard.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-stdout-denial-guard

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @argszero/dsh-stdout-denial-guard`
- npm registry：https://registry.npmjs.org/@argszero/dsh-stdout-denial-guard
- Node 要求：^22.19 || >=24
