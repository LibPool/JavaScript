# @streamapp/douyin

> 标签: stream-recipe

## 简介

抖音 — replay 采集源（跑在用户自己的 Chrome 上）。 搜索走登录态浏览器：直达搜索结果页，拦页面自己发的 general/search/single XHR。 （站外 HTTP 搜索端点被风控门挡着——无 cookie 返回 status_code 2483「请先登录」， 而登录 cookie 有 7KB+、塞进 query 会被上游拒；所以这条只能在浏览器里走。）

## 官网

- npm 页面：https://www.npmjs.com/package/@streamapp/douyin

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install @streamapp/douyin`
- npm registry：https://registry.npmjs.org/@streamapp/douyin
