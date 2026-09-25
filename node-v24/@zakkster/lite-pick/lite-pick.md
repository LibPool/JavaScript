# @zakkster/lite-pick

> 标签: alias-method, anti-flapping, balancer, bounded-load, circuit-breaker, client-side-load-balancing, consistent-hash, consistent-hashing, deterministic, endpoint-selection, esm, fail-closed, garbage-collection, gc, health-check, high-throughput, hysteresis, in-process, latency-aware, least-conn, least-connections, lightweight, load-balance, load-balancer, load-balancing, maglev, never-queue, p2c, peak-ewma, performance, pick, power-of-two-choices, prng, round-robin, sed, selection, server-selection, shortest-expected-delay, smooth-weighted-round-robin, sticky, sticky-routing, tree-shakeable, two-random-choices, typed-array, vose, weighted-random, weighted-round-robin, worker-pool, wrr, xorshift32, zero-allocation, zero-dependency, zero-gc

## 简介

Zero-dependency, zero-GC load-balancing selection kernel: one hot pick() -> endpoint index over a fixed pool, 0 B/op steady-state. A pure selector (consumes health/circuit state, never a proxy) for the in-process hop, complementary to AWS NLB/ALB. Tree-sh

## 官网

- 官网：https://github.com/PeshoVurtoleta/lite-pick#readme
- 源码仓库：git+https://github.com/PeshoVurtoleta/lite-pick.git
- npm 页面：https://www.npmjs.com/package/@zakkster/lite-pick

## 历史版本号

- 当前版本：1.0.0

- 0.1.0
- 0.2.0
- 0.3.0
- 0.4.0
- 0.5.0
- 0.6.0
- 0.7.0
- 0.7.1
- 0.7.2
- 0.8.0
- 0.9.0
- 1.0.0

## 获取地址

- npm 安装：`npm install @zakkster/lite-pick`
- npm registry：https://registry.npmjs.org/@zakkster/lite-pick
- Node 要求：>=18
