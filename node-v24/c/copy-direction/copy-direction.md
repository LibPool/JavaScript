# copy-direction

> 标签: JavaScript

## 简介

const copyFn = (agoPath, nowPath) => {     //容错处理     if (!fs.existsSync(agoPath)) {         console.log("您需要复制的文件夹不存在");         return;     }     if (fs.existsSync(nowPath)) {         console.log("您可能已经复制完成！！！")         return;     }     //创建新

## 官网

- npm 页面：https://www.npmjs.com/package/copy-direction

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install copy-direction`
- npm registry：https://registry.npmjs.org/copy-direction
