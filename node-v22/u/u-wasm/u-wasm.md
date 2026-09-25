# u-wasm

> 标签: JavaScript

## 简介

```ts import { createWasm,useCCall,useCWrap } from "u-wasm"; import { readFileSync } from "fs"; const buf = readFileSync("./math.wasm"); const cwrap = useCWrap(); const ccall = useCCall(); const w = await createWasm(buf); const wasm = w.use(cwrap).

## 官网

- npm 页面：https://www.npmjs.com/package/u-wasm

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install u-wasm`
- npm registry：https://registry.npmjs.org/u-wasm
