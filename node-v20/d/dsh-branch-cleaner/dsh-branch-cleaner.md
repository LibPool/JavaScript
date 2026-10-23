# dsh-branch-cleaner

> 标签: branch, branches, cleanup, deepseek-harness, dsh, dsh-plugin, dsh-web, git, merged-branches, prune, squash-merge, stale-branches, 冗余分支, 分支清理, 已合并分支

## 简介

DeepSeek Harness 的冗余分支清理工具：找出已经落地到主线的 git 分支（普通合并 / squash 合并 / rebase 落地 / 上游已删 / PR 已合并）并可一键删除，默认只报告、删除前自动备份到 refs/backup/branch-cleaner/。Branch cleaner plugin for DSH — detect merged, squash-merged, patch-equivalent, upstream-gone and PR-merged branche

## 官网

- 官网：https://github.com/ramwin/dsh-branch-cleaner#readme
- 源码仓库：git+https://github.com/ramwin/dsh-branch-cleaner.git
- npm 页面：https://www.npmjs.com/package/dsh-branch-cleaner

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-branch-cleaner`
- npm registry：https://registry.npmjs.org/dsh-branch-cleaner
- Node 要求：>=20
