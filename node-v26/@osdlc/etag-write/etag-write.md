# @osdlc/etag-write

> 标签: atomic, cas, compare-and-swap, durability, etag, fsync, lost-update, rename, typescript, write

## 简介

Atomic file writes, sha256 etags and compare-and-swap: a temp file in the same directory, fsync, rename, fsync the directory, so a reader never sees a torn file and a crash never leaves one. CAS refuses a blind overwrite.

## 官网

- 官网：https://github.com/osdlc/osdlc/tree/main/packages/ts/etag-write#readme
- 源码仓库：git+https://github.com/osdlc/osdlc.git
- npm 页面：https://www.npmjs.com/package/@osdlc/etag-write

## 历史版本号

- 当前版本：0.2.1

- 0.0.0-stage
- 0.0.1-stage
- 0.2.0
- 0.2.1

## 获取地址

- npm 安装：`npm install @osdlc/etag-write`
- npm registry：https://registry.npmjs.org/@osdlc/etag-write
- Node 要求：>=22
