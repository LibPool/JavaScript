# @mikasomaka/dsh-web-search

> 标签: cordis, deepseek-harness, dsh, exa, fallback, firecrawl, gemini, google-search, grounding, multi-provider, plugin, search-provider, web-search, websearch

## 简介

多 provider 顺序链的 web_search 后端（DeepSeek Harness 插件）：给内置 web_search 工具注册一个 chain provider，按顺序回退 Gemini（Google Search grounding）、Exa、Firecrawl。key 与配置全在 ~/.dsh/settings.yaml，复用内置工具的 schema/渲染/UI，无需新工具。

## 官网

- npm 页面：https://www.npmjs.com/package/@mikasomaka/dsh-web-search

## 历史版本号

- 当前版本：0.1.3

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3

## 获取地址

- npm 安装：`npm install @mikasomaka/dsh-web-search`
- npm registry：https://registry.npmjs.org/@mikasomaka/dsh-web-search
- Node 要求：>=18.17.0
