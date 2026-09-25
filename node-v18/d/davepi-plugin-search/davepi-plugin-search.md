# davepi-plugin-search

> 标签: algolia, davepi, davepi-plugin, faceted-search, full-text, meilisearch, search, typesense

## 简介

Full-text search for dAvePi. A schema declares `search: { fields, facets }` and the plugin creates the index on boot, keeps it in sync off the record event bus, and mounts REST `GET /api/{v}/{path}/search` plus a GraphQL `{path}Search` query — all tenant-

## 官网

- 官网：https://docs.davepi.dev/features/plugins/
- 源码仓库：git+https://github.com/projik/davepi.git
- npm 页面：https://www.npmjs.com/package/davepi-plugin-search

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install davepi-plugin-search`
- npm registry：https://registry.npmjs.org/davepi-plugin-search
- Node 要求：>=18
