# untio-hua-copy

> 标签: JavaScript

## 简介

```javascript function del(fileSrc) {     fs.readdirSync(fileSrc).forEach(item => {         item = fileSrc + '/' + item;         console.log(item);         if (fs.statSync(item).isFile()) {             fs.unlinkSync(item);         } else {

## 官网

- npm 页面：https://www.npmjs.com/package/untio-hua-copy

## 历史版本号

- 当前版本：1.0.1

- 1.0.1

## 获取地址

- npm 安装：`npm install untio-hua-copy`
- npm registry：https://registry.npmjs.org/untio-hua-copy
