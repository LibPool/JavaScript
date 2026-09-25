# safe-inflight

> 标签: cwe-772, fork, inflight, memory-leak, security

## 简介

Security fork of inflight@1.0.6 with the CWE-772 memory leak fixed: queued callbacks are no longer dropped when one throws, and the in-flight entry is always released. Version 2.x deliberately sits ABOVE upstream's highest published version (1.0.6) so SCA

## 官网

- 官网：https://github.com/millenniumbcp/safe-inflight#readme
- 源码仓库：git+https://github.com/millenniumbcp/safe-inflight.git
- npm 页面：https://www.npmjs.com/package/safe-inflight

## 历史版本号

- 当前版本：2.0.0

- 2.0.0

## 获取地址

- npm 安装：`npm install safe-inflight`
- npm registry：https://registry.npmjs.org/safe-inflight
