# @argszero/dsh-destructive-command-guard

> 标签: cordis, deepseek-harness, destructive, dsh, fs, guard, plugin, powershell, pre-execute, remove-item, rm, safety, shell, tools, windows

## 简介

Refuses a shell command before it runs when it deletes something it did not name. In PowerShell variable names are case-insensitive and the automatic variables are read-only, so `$home = "<scratch>"` followed by `Remove-Item $home -Recurse -Force` removes

## 官网

- 官网：https://github.com/argszero/dsh-destructive-command-guard#readme
- 源码仓库：git+https://github.com/argszero/dsh-destructive-command-guard.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-destructive-command-guard

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @argszero/dsh-destructive-command-guard`
- npm registry：https://registry.npmjs.org/@argszero/dsh-destructive-command-guard
- Node 要求：^22.19 || >=24
