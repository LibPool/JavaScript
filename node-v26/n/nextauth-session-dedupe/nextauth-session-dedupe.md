# nextauth-session-dedupe

> 标签: auth.js, authjs, broadcastchannel, cache, dedupe, fetch, next-auth, nextauth, performance, request-coalescing, session

## 简介

Drop-in fix for NextAuth v5 / Auth.js firing duplicate GET /api/auth/session requests on every page load. Dedupes at the fetch layer with a short TTL cache and in-flight promise coalescing.

## 官网

- 官网：https://github.com/Aman-456/nextauth-session-dedupe#readme
- 源码仓库：git+https://github.com/Aman-456/nextauth-session-dedupe.git
- npm 页面：https://www.npmjs.com/package/nextauth-session-dedupe

## 历史版本号

- 当前版本：0.3.0

- 0.1.0
- 0.2.0
- 0.3.0

## 获取地址

- npm 安装：`npm install nextauth-session-dedupe`
- npm registry：https://registry.npmjs.org/nextauth-session-dedupe
- Node 要求：>=18
