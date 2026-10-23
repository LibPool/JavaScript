# pi-llama-slot-isolation

> 标签: concurrency, extension, kv-cache, llama.cpp, llamacpp, local-first, pi, pi-coding-agent, pi-package, slots

## 简介

Prevents concurrent pi sessions from clobbering each other's llama.cpp KV cache — each session is pinned to the best available slot (empty > cold > low tokens > low id) via the server's /slots endpoint, coordinated across windows through a state file

## 官网

- 官网：https://github.com/driderr/pi-llama-slot-isolation#readme
- 源码仓库：git+https://github.com/driderr/pi-llama-slot-isolation.git
- npm 页面：https://www.npmjs.com/package/pi-llama-slot-isolation

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install pi-llama-slot-isolation`
- npm registry：https://registry.npmjs.org/pi-llama-slot-isolation
