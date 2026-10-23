# @argszero/dsh-upload-index-cache

> 标签: attachments, cache, cordis, deepseek-harness, dsh, files-api, images, llm-deepseek, memoize, performance, plugin, upload-index

## 简介

Resolving a retained image to its DeepSeek file id re-reads and re-validates the whole upload index, once per image per HTTP attempt: DeepSeekUploadIndex.get() calls load(), which reads files-v3.json and runs its parser over every record. Measured on the

## 官网

- 官网：https://github.com/argszero/dsh-upload-index-cache#readme
- 源码仓库：git+https://github.com/argszero/dsh-upload-index-cache.git
- npm 页面：https://www.npmjs.com/package/@argszero/dsh-upload-index-cache

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @argszero/dsh-upload-index-cache`
- npm registry：https://registry.npmjs.org/@argszero/dsh-upload-index-cache
- Node 要求：^22.19 || >=24
