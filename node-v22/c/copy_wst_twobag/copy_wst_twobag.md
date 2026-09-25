# copy_wst_twobag

> 标签: JavaScript

## 简介

```javascript let fs = require("fs"); const copyDir = (sorDir,tarDir)=>{     if(!fs.existsSync(sorDir)){         throw new Error("不存在复制路径" + sorDir);     }     if(fs.existsSync(tarDir)){         throw new Error("已经存在该目标路径啦" + tarDir);     }     f

## 官网

- npm 页面：https://www.npmjs.com/package/copy_wst_twobag

## 历史版本号

- 当前版本：1.0.5

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.5

## 获取地址

- npm 安装：`npm install copy_wst_twobag`
- npm registry：https://registry.npmjs.org/copy_wst_twobag
