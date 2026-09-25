# bun-minhook

> 标签: detour, exoproc, function-hooking, hook, minhook, systems-instrumentation, trampoline, windows, x64

## 简介

MinHook-style trampoline/detour function hooking for Bun. Unlike nhook (no allocation, 2-byte inline patch), this builds a real relocated trampoline and installs a 5-byte JMP detour, with the detour itself supplied as caller-provided machineCode for cross

## 官网

- 官网：https://github.com/woldann/exoproc#readme
- 源码仓库：git+https://github.com/woldann/exoproc.git
- npm 页面：https://www.npmjs.com/package/bun-minhook

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install bun-minhook`
- npm registry：https://registry.npmjs.org/bun-minhook
