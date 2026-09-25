# @unbrowse/puppeteer-shim

> 标签: chrome, headless, puppeteer, scraping, shim, unbrowse

## 简介

Drop-in replacement for puppeteer. page.goto() short-circuits through Unbrowse's resolved-route cache ($0 on hit) and falls through to real puppeteer on miss — same launch/newPage/goto/content surface, pay per cached call instead of per browser-hour.

## 官网

- 官网：https://unbrowse.ai/vs/puppeteer
- 源码仓库：git+https://github.com/unbrowse-ai/unbrowse.git
- npm 页面：https://www.npmjs.com/package/@unbrowse/puppeteer-shim

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install @unbrowse/puppeteer-shim`
- npm registry：https://registry.npmjs.org/@unbrowse/puppeteer-shim
