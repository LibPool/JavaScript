# brotli-polyfill

> 标签: CVE-2026-111497, brotli, decompression, mitigation, security, zlib

## 简介

Fail-safe Brotli decompression shim for Node runtimes with an unpatched native decoder (CVE-2026-111497). Routes Brotli decoding through the patched decoder sandboxed in WebAssembly (pure-JS fallback), as an interim mitigation until the runtime is upgrade

## 官网

- 官网：https://github.com/carlosroberto555/brotli-polyfill#readme
- 源码仓库：git+https://github.com/carlosroberto555/brotli-polyfill.git
- npm 页面：https://www.npmjs.com/package/brotli-polyfill

## 历史版本号

- 当前版本：1.0.0

- 0.0.0-stage
- 1.0.0

## 获取地址

- npm 安装：`npm install brotli-polyfill`
- npm registry：https://registry.npmjs.org/brotli-polyfill
- Node 要求：>=10
