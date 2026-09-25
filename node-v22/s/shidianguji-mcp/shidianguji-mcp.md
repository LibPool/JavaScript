# shidianguji-mcp

> 标签: ancient-books, chinese-literature, mcp, playwright, server, shidianguji

## 简介

史典古籍 MCP Server - 提供古籍搜索、分类浏览、书籍获取等功能的 MCP 服务器

v0.3.0 史诗级更新（百万字长文本智能分块系统）：

📦 智能分块系统：
- 500字/块：对应古籍一页，支持百万字级别文本
- 三种模式：默认模式、关键词搜索、精确获取
- LLM友好：<书籍信息>、<块N>标签清晰结构化

🚀 高性能缓存：
- 智能缓存：首次3-4秒，缓存命中0ms
- LRU策略：1小时TTL，10分钟自动清理
- 访问续期：常用内容自动保持缓存

✨ 核心特性：
- 关键词检索

## 官网

- 官网：https://github.com/yokami618/history#readme
- 源码仓库：git+https://github.com/yokami618/history.git
- npm 页面：https://www.npmjs.com/package/shidianguji-mcp

## 历史版本号

- 当前版本：0.3.0

- 0.1.12
- 0.1.13
- 0.1.14
- 0.1.2
- 0.1.3
- 0.1.4
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.8
- 0.1.9
- 0.3.0

## 获取地址

- npm 安装：`npm install shidianguji-mcp`
- npm registry：https://registry.npmjs.org/shidianguji-mcp
- Node 要求：>=18
