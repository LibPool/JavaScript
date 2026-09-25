# @streamapp/bt0

> 标签: stream-recipe

## 简介

bt0(不太灵影视)— 纯 http recipe。站点从 (1-9)bt0.com 搬到 web{n}.mukaku.com（Vue SPA）， 数据走 JSON API `/prod/api/v1/`；每请求必带站点 JS 写死的常量 app_id + identity（axios 拦截器 逐请求追加，非按访客生成，照抄即站点自身行为）。迁自本地 RSSHub 路由 lib/routes/bt0/{tlist,search}.ts。 domain 固定 web2（2/3/5 可达，默认 2）；站方换掉

## 官网

- npm 页面：https://www.npmjs.com/package/@streamapp/bt0

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install @streamapp/bt0`
- npm registry：https://registry.npmjs.org/@streamapp/bt0
