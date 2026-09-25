# @kanamone/edge-scrambler

> 标签: JavaScript

## 简介

## dist/index.js ```js function createScrambler(b, a, c, w, t) {   const f = (e, u) => new Array(e).fill(0).map((n, r) => u(r)), A = (e, u, n) => {     let r = n;     return f(u, () => f(e, () => (r ^= r << 13, r ^= r >> 17, r ^= r << 5)).map((m, o) => [m

## 官网

- 官网：https://github.com/kanamone/edge-scrambler
- npm 页面：https://www.npmjs.com/package/@kanamone/edge-scrambler

## 历史版本号

- 当前版本：0.0.3

- 0.0.1
- 0.0.2
- 0.0.3

## 获取地址

- npm 安装：`npm install @kanamone/edge-scrambler`
- npm registry：https://registry.npmjs.org/@kanamone/edge-scrambler
