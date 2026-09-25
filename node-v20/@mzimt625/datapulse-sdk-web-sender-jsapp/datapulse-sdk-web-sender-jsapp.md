# @mzimt625/datapulse-sdk-web-sender-jsapp

> 标签: JavaScript

## 简介

自定义存储与发送时机的 Sender。宿主实现 `storage.append/drain/restore`，可写入 IndexedDB、App Bridge 或业务队列；调用 `flush()` 时交给下游 Sender 并排空下游缓冲。下游拒绝 payload 时会恢复尚未转移的数据。

## 官网

- npm 页面：https://www.npmjs.com/package/@mzimt625/datapulse-sdk-web-sender-jsapp

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @mzimt625/datapulse-sdk-web-sender-jsapp`
- npm registry：https://registry.npmjs.org/@mzimt625/datapulse-sdk-web-sender-jsapp
