# @streamapp/tencent

> 标签: stream-recipe

## 简介

腾讯视频（v.qq.com）— 纯 http recipe（pbaccess.video.qq.com）。 episode：GetPageData 走 page_id:vsite_episode_list，明文 JSON、无签名，UA/Origin 均非必需（不同于 该站 search 端点——那个端点缺这两个头会被拒 20607，此处不需要）。page_size=100 通常一页拿全； compute.decode 把 module_list_datas 摊平成 items[]，并把 module_pa

## 官网

- npm 页面：https://www.npmjs.com/package/@streamapp/tencent

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install @streamapp/tencent`
- npm registry：https://registry.npmjs.org/@streamapp/tencent
