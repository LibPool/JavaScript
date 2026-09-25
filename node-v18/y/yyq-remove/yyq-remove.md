# yyq-remove

> 标签: JavaScript

## 简介

```js const fs=require('fs'); const removeDir=(pathDir)=>{     //查找文件夹子目录     const arr=fs.readdirSync(pathDir);     //遍历     arr.forEach(item=>{         item=pathDir+"/"+item;//拼接路径         const info=fs.statSync(item);//查看文件信息         if(info.i

## 官网

- npm 页面：https://www.npmjs.com/package/yyq-remove

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install yyq-remove`
- npm registry：https://registry.npmjs.org/yyq-remove
