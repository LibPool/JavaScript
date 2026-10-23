# @zukhruf/sqlite-snapshot

> 标签: node-sqlite, read-only, read-transaction, snapshot, sqlite, wal

## 简介

A read-only snapshot of a SQLite database that another process owns and writes. It pins one moment with a read transaction, so the tables agree, and it never opens the file immutable, so it sees the newest rows in the WAL. It checks the columns that a rea

## 官网

- 官网：https://github.com/JanuaryLabs/zukhruf/tree/main/packages/sqlite/snapshot#readme
- 源码仓库：git+https://github.com/JanuaryLabs/zukhruf.git
- npm 页面：https://www.npmjs.com/package/@zukhruf/sqlite-snapshot

## 历史版本号

- 当前版本：0.3.40

- 0.0.0-stage
- 0.3.31
- 0.3.32
- 0.3.33
- 0.3.34
- 0.3.35
- 0.3.36
- 0.3.37
- 0.3.38
- 0.3.39
- 0.3.40

## 获取地址

- npm 安装：`npm install @zukhruf/sqlite-snapshot`
- npm registry：https://registry.npmjs.org/@zukhruf/sqlite-snapshot
