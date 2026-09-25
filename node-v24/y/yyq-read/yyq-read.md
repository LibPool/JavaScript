# yyq-read

> 标签: JavaScript

## 简介

```js const fs=require('fs'); class ReadFile{       constructor(options){           Object.assign(this,{},options);           const info=fs.statSync(this.pathfile);           if(info.isFile()){               const a=fs.readFileSync(this.pathfile,"u

## 官网

- npm 页面：https://www.npmjs.com/package/yyq-read

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install yyq-read`
- npm registry：https://registry.npmjs.org/yyq-read
