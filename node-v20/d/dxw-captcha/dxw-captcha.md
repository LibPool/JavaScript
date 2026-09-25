# dxw-captcha

> 标签: JavaScript

## 简介

``` npm i dxw-captcha -S ``` #使用 ``` const http =require("http") const ptcha=require("dxw-captcha") http.createServer((req,res)=>{     let captcha=ptcha.create()     res.setHeader("content-type","text/html;charset=utf-8")     res.end(captcha.dat

## 官网

- npm 页面：https://www.npmjs.com/package/dxw-captcha

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install dxw-captcha`
- npm registry：https://registry.npmjs.org/dxw-captcha
