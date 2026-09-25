# @zakkster/lite-aabb

> 标签: 2d, aabb, allocation-free, axis-aligned, bounding-box, broadphase, canvas, collision, float32array, game-dev, geometry, math, spatial, twitch-extension, typed-array, webgl, webgpu, zero-gc

## 简介

Zero-GC 2D axis-aligned bounding box primitives. 22 ops on a flat Float32Array(4) [minX, minY, maxX, maxY], including packed 4xN batch ops; every op writes into a caller-provided out buffer — no per-frame allocation. ~230 lines, zero deps, ESM only.

## 官网

- 官网：https://github.com/PeshoVurtoleta/lite-aabb#readme
- 源码仓库：git+https://github.com/PeshoVurtoleta/lite-aabb.git
- npm 页面：https://www.npmjs.com/package/@zakkster/lite-aabb

## 历史版本号

- 当前版本：2.0.0

- 1.0.0
- 1.0.1
- 1.0.2
- 1.1.0
- 1.2.0
- 1.3.0
- 2.0.0

## 获取地址

- npm 安装：`npm install @zakkster/lite-aabb`
- npm registry：https://registry.npmjs.org/@zakkster/lite-aabb
- Node 要求：>=18
