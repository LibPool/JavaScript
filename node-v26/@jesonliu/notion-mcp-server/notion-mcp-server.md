# @jesonliu/notion-mcp-server

> 标签: JavaScript

## 简介

Notion MCP server：封装 Notion REST API（查询数据库/搜索页面/读写页面/追加块/动态读取数据库 schema），供 idea-collector 等 skill 使用。v0.6 移除三个固定 DB ID 配置（NOTION_KNOWLEDGE_DB_ID / PROJECT_DB_ID / MATERIAL_DB_ID），改为单一根页面 ID（NOTION_ROOT_PAGE_ID）+ 新增 notion_list_databases 工具，启动时自动列举页面下数据库供

## 官网

- npm 页面：https://www.npmjs.com/package/@jesonliu/notion-mcp-server

## 历史版本号

- 当前版本：0.6.1

- 0.2.0
- 0.3.0
- 0.4.0
- 0.5.0
- 0.6.1

## 获取地址

- npm 安装：`npm install @jesonliu/notion-mcp-server`
- npm registry：https://registry.npmjs.org/@jesonliu/notion-mcp-server
- Node 要求：>=18
