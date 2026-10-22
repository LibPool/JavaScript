# @broberg/greppable

> 标签: audit, binary-detection, broberg, ci, encoding, false-green, grep, latin-1, lint, nul-byte, ripgrep, ugrep, utf-8

## 简介

Find the tracked text files your grep silently skips. A cc session's grep is ugrep with -I: on a file with a NUL byte or invalid UTF-8 it prints nothing and exits 1, so every grep-based sweep over that file is falsely green. Zero deps, one bin, runs in an

## 官网

- 官网：https://github.com/broberg-ai/components#readme
- 源码仓库：git+https://github.com/broberg-ai/components.git
- npm 页面：https://www.npmjs.com/package/@broberg/greppable

## 历史版本号

- 当前版本：0.3.0

- 0.1.0
- 0.1.1
- 0.2.0
- 0.3.0

## 获取地址

- npm 安装：`npm install @broberg/greppable`
- npm registry：https://registry.npmjs.org/@broberg/greppable
