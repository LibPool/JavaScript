# yyq-pagedemo

> 标签: JavaScript

## 简介

```js const express=require('express'); const app=express(); const fs=require('fs'); app.listen(8888,()=>console.log('开启')) app.use(express.static('public')) app.set('view engine',"ejs") app.get('/',(req,res)=>{     res.render('index') })

## 官网

- npm 页面：https://www.npmjs.com/package/yyq-pagedemo

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install yyq-pagedemo`
- npm registry：https://registry.npmjs.org/yyq-pagedemo
