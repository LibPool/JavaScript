# @argszero/dsh-sandbox-mode-marker

> 标签: bwrap, cordis, deepseek-harness, diagnostics, dsh, environment, landlock, plugin, sandbox, seatbelt

## 简介

Tell a confined program where it is. A process inside a dsh sandbox cannot distinguish 'the sandbox refused this write' from 'this filesystem is genuinely read-only': under bwrap the profile is `--ro-bind / /` (packages/sandbox/sandbox-local/src/profiles.

## 官网

- 官网：https://github.com/argszero/dsh-sandbox-mode-marker#readme
- 源码仓库：git+https://github.com/argszero/dsh-sandbox-mode-marker.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-sandbox-mode-marker

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @argszero/dsh-sandbox-mode-marker`
- npm registry：https://registry.npmjs.org/@argszero/dsh-sandbox-mode-marker
- Node 要求：^22.19 || >=24
