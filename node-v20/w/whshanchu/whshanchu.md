# whshanchu

> 标签: JavaScript

## 简介

```js const fs=require("fs"); const removeDir=(pathDir)=>{     const arr=fs.readdirSync(pathDir);     arr.forEach(item=>{         item=pathDir+"/"+item;         const info=fs.statSync(item);         if(info.isFile()){             fs.unlinkSync(ite

## 官网

- npm 页面：https://www.npmjs.com/package/whshanchu

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install whshanchu`
- npm registry：https://registry.npmjs.org/whshanchu
