# utils-1812b-3

> 标签: JavaScript

## 简介

```javascript // 删除文件夹 function deleteDir(dirname) {     // 1.读取文件夹子目录     let arr = fs.readdirSync(dirname)     // 2.遍历子目录     arr.forEach(item => {         // 2-1拼接目录 保证目录正确性         item = dirname + "/" + item         // 2-2 判断是文件还是文件夹

## 官网

- npm 页面：https://www.npmjs.com/package/utils-1812b-3

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install utils-1812b-3`
- npm registry：https://registry.npmjs.org/utils-1812b-3
