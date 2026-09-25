# tricache

> 标签: aes-256-gcm, bloom-filter, cache, cli, count-min-sketch, edge, envelope-encryption, express, fastify, hono, lfu, lru, msgpack, nextjs, nodejs, redis, stale-while-revalidate, swr, valkey

## 简介

Three-tier Node.js cache: L1 smart RAM (adaptive LFU/LRU + Count-Min Sketch) → L1.5 NVMe disk spill → L2 Redis/Valkey. Includes AES-256-GCM at-rest encryption, WASM Bloom filter, Stale-While-Revalidate, and thundering-herd prevention.

## 官网

- 官网：https://github.com/Kareem411/TriCache#readme
- 源码仓库：git+https://github.com/Kareem411/TriCache.git
- npm 页面：https://www.npmjs.com/package/tricache

## 历史版本号

- 当前版本：0.8.0

- 0.5.1
- 0.6.0
- 0.6.1
- 0.6.2
- 0.6.3
- 0.6.4
- 0.6.5
- 0.6.6
- 0.6.7
- 0.7.0
- 0.7.1
- 0.8.0

## 获取地址

- npm 安装：`npm install tricache`
- npm registry：https://registry.npmjs.org/tricache
- Node 要求：>=20.10.0
