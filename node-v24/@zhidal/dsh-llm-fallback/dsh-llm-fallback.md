# @zhidal/dsh-llm-fallback

> 标签: JavaScript

## 简介

dsh-llm-fallback 插件：拦截全局 LLM 调用，会话指定的模型（事实主模型）失败时按 fallbackChains 纯回退队列自动切换到下一个候选 provider/model。retriesBeforeSwitch 控制每候选切换前的同 provider 重试次数（默认 0=跟随官方 dsh-llm-retry 预算；N>0=以插件为准，超出官方预算部分由插件代执行），对话不中断。

## 官网

- 官网：https://github.com/lzhida/dsh-plugins-workspace/tree/main/packages/dsh-llm-fallback#readme
- 源码仓库：git+https://github.com/lzhida/dsh-plugins-workspace.git
- npm 页面：https://www.npmjs.com/package/@zhidal/dsh-llm-fallback

## 历史版本号

- 当前版本：0.5.0

- 0.3.0
- 0.3.1
- 0.4.0
- 0.5.0

## 获取地址

- npm 安装：`npm install @zhidal/dsh-llm-fallback`
- npm registry：https://registry.npmjs.org/@zhidal/dsh-llm-fallback
