# yyq-demo

> 标签: JavaScript

## 简介

```js const fs=require('fs'); const copy=(sourcePath,targetPath)=>{     const flay1=fs.existsSync(sourcePath);     const flay2=fs.existsSync(targetPath);     //容错     if(!flay1){         throw new Error('源文件不存在'+sourcePath);         return;     }

## 官网

- npm 页面：https://www.npmjs.com/package/yyq-demo

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install yyq-demo`
- npm registry：https://registry.npmjs.org/yyq-demo
