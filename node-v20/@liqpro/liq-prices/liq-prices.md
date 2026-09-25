# @liqpro/liq-prices

> 标签: JavaScript

## 简介

Поток цен биржи для браузера: `LiqPrices` держит одну подписку на SSE шлюза (`/sse?channels=price:<marketId>,…`), переоткрывает её с backoff по ошибке или тишине и отдаёт троттлированные `prices_updated`. Стартовое значение — `GET /markets/:id/price`.

## 官网

- npm 页面：https://www.npmjs.com/package/@liqpro/liq-prices

## 历史版本号

- 当前版本：0.57.0

- 0.46.0
- 0.47.0
- 0.47.1
- 0.48.0
- 0.49.0
- 0.50.0
- 0.52.0
- 0.53.0
- 0.54.0
- 0.55.0
- 0.56.0
- 0.57.0

## 获取地址

- npm 安装：`npm install @liqpro/liq-prices`
- npm registry：https://registry.npmjs.org/@liqpro/liq-prices
