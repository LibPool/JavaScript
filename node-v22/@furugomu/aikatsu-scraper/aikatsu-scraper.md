# @furugomu/aikatsu-scraper

> 标签: JavaScript

## 简介

```js async () => {   const fetch = require("node-fetch");   const { scrapeFriends } = require("@furugomu/aikatsu-scraper");   const html = (await fetch(     "http://www.aikatsu.com/friends/cardlist/detail.php?id=137233"   )).text();   console.log(scrapeF

## 官网

- 官网：https://github.com/furugomu/aikatsu-scraper#readme
- 源码仓库：git+https://github.com/furugomu/aikatsu-scraper.git
- npm 页面：https://www.npmjs.com/package/@furugomu/aikatsu-scraper

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install @furugomu/aikatsu-scraper`
- npm registry：https://registry.npmjs.org/@furugomu/aikatsu-scraper
