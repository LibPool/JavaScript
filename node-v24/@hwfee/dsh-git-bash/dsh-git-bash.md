# @hwfee/dsh-git-bash

> 标签: deepseek, deepseek-harness, dsh, dsh-plugin, git-bash, shell, windows

## 简介

DeepSeek Harness 的 Git Bash 默认 shell：把 Windows 上的默认命令解释器从 PowerShell 换成 Git Bash，并暴露一个 run_shell 工具。自动从 git --exec-path 定位 Git Bash（WSL 的 bash 不算），找不到时降级而不是让插件消失。 / Git Bash as the default shell for DeepSeek Harness on Windows: resolves Git Bash from `git

## 官网

- npm 页面：https://www.npmjs.com/package/@hwfee/dsh-git-bash

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @hwfee/dsh-git-bash`
- npm registry：https://registry.npmjs.org/@hwfee/dsh-git-bash
- Node 要求：^22.19.0 || >=24.0.0
