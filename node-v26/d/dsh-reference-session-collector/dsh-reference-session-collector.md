# dsh-reference-session-collector

> 标签: deepseek-harness, dsh, dsh-plugin, fts5, projection, search, session, sqlite, tokenizer

## 简介

DSH Web 插件：会话原文投影同步器（DRS）——只读扫描 ~/.dsh/sessions 会话日志，解码后投影进自有 SQLite（segments/replaces/FTS5），经 /api/dsh-reference-session-collector 提供 surface 标记、召回对账与内容检索面。绝不写会话文件。

## 官网

- 官网：https://github.com/drscrewdriver/dsh-reference-session-collector#readme
- 源码仓库：git+https://github.com/drscrewdriver/dsh-reference-session-collector.git
- npm 页面：https://www.npmjs.com/package/dsh-reference-session-collector

## 历史版本号

- 当前版本：0.2.0

- 0.0.0-stage
- 0.1.0
- 0.2.0
- 0.2.0-beta.0

## 获取地址

- npm 安装：`npm install dsh-reference-session-collector`
- npm registry：https://registry.npmjs.org/dsh-reference-session-collector
- Node 要求：>=22
