# @c0dingbear/chromium-idb-reader

> 标签: chromium, forensics, idb_cmp1, indexeddb, leveldb, pure-js, snappy, sstable

## 简介

Pure-JS reader for Chromium IndexedDB LevelDB stores (the idb_cmp1 databases that level/leveldown can't open). Parses .log + .ldb SSTables, decompresses Snappy, and returns current (last-write-wins) records with their sequence numbers. Zero native depende

## 官网

- npm 页面：https://www.npmjs.com/package/@c0dingbear/chromium-idb-reader

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @c0dingbear/chromium-idb-reader`
- npm registry：https://registry.npmjs.org/@c0dingbear/chromium-idb-reader
- Node 要求：>=16
