# @jeebey/wx-singleflight

> 标签: JavaScript

## 简介

async fnLoginOpenid() {     return sf.do('fnLoginOpenid', async () => {       const { code } = await wx.login()       console.log("res", code)       const res = await App.$http.post('/wx/openid', { code })       console.log("res", res)       return

## 官网

- npm 页面：https://www.npmjs.com/package/@jeebey/wx-singleflight

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install @jeebey/wx-singleflight`
- npm registry：https://registry.npmjs.org/@jeebey/wx-singleflight
