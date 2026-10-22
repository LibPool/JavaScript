# @argszero/cordis-plugin-session-query-read-guard

> 标签: cordis, deepseek-harness, diagnostics, dsh, host-freeze, plugin, readevent, session, session-query, structuredclone

## 简介

Read-pressure guard for dsh session history: every ctx.sessionQuery per-session read materializes and deep-clones the whole session, and readEvent is documented as a bounded single-event read while costing O(session) to build it. A consumer that reads onc

## 官网

- 官网：https://github.com/argszero/cordis-plugin-session-query-read-guard#readme
- 源码仓库：git+https://github.com/argszero/cordis-plugin-session-query-read-guard.git
- npm 页面：https://www.npmjs.com/package/@argszero/cordis-plugin-session-query-read-guard

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @argszero/cordis-plugin-session-query-read-guard`
- npm registry：https://registry.npmjs.org/@argszero/cordis-plugin-session-query-read-guard
