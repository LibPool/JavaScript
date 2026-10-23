# dsh-delete-guard

> 标签: deepseek-harness, dsh, dsh-plugin, guardrails, hooks, recycle-bin, safe-delete, trash, undelete, windows

## 简介

Force every DSH file deletion through the OS Recycle Bin. Intercepts shell tool calls at tools/pre-execute (pwsh, bash, cmd, the persistent terminal), rewrites destructive delete commands into a recoverable recycle-bin move (Win32 SHFileOperation / SHQuer

## 官网

- 官网：https://github.com/deepestevan/dsh-delete-guard#readme
- 源码仓库：git+https://github.com/deepestevan/dsh-delete-guard.git
- npm 页面：https://www.npmjs.com/package/dsh-delete-guard

## 历史版本号

- 当前版本：2.2.3

- 0.0.0-stage
- 2.2.3

## 获取地址

- npm 安装：`npm install dsh-delete-guard`
- npm registry：https://registry.npmjs.org/dsh-delete-guard
- Node 要求：>=20.0.0
