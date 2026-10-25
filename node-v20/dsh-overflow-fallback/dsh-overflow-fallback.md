# dsh-overflow-fallback

> 标签: compaction, context-window, deepseek-harness, dsh, dsh-plugin, handoff, recovery, revive, session

## 简介

溢出兜底与续命：上下文超限、内置压缩放弃后自动再压一次并重试；仍失败时把原会话整理成交接包，在新会话接着聊。不换引擎、不加界面；续命默认显式触发，原会话只读。 · Overflow fallback and session revival for DeepSeek Harness: one last compaction retry, then continue the dead session in a fresh one with a handoff. No engine swap, no UI, o

## 官网

- 官网：https://github.com/WALZX123/dsh-overflow-fallback#readme
- 源码仓库：git+https://github.com/WALZX123/dsh-overflow-fallback.git
- npm 页面：https://www.npmjs.com/package/dsh-overflow-fallback

## 历史版本号

- 当前版本：0.4.0

- 0.0.0-stage
- 0.4.0

## 获取地址

- npm 安装：`npm install dsh-overflow-fallback`
- npm registry：https://registry.npmjs.org/dsh-overflow-fallback
- Node 要求：>=20
