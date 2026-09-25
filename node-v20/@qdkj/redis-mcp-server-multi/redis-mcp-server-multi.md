# @qdkj/redis-mcp-server-multi

> 标签: cache, key-value, mcp, model-context-protocol, multi-connection, redis

## 简介

多连接版 Redis MCP 服务端；基于 @qdkj/redis-mcp-server v1.0.4，单 server 实例承载 N 个 Redis 连接，工具层显式 conn 参数路由 + 9 条黑名单（unique 8 + 1 重复 FLUSHDB）+ 14 条白名单子集 二重控制。

## 官网

- npm 页面：https://www.npmjs.com/package/@qdkj/redis-mcp-server-multi

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install @qdkj/redis-mcp-server-multi`
- npm registry：https://registry.npmjs.org/@qdkj/redis-mcp-server-multi
- Node 要求：>=18.0.0
