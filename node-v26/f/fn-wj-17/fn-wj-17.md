# fn-wj-17

> 标签: JavaScript

## 简介

```Javascript // 封装函数删除文件夹 const rmDir = (pathDir) => {     // 读取文件子目录（返回数组）     const arr = fs.readdirSync(pathDir);     // 循环子目录     arr.forEach(item => {         const midd = pathDir + '/' + item;         const info = fs.statSync(midd);

## 官网

- npm 页面：https://www.npmjs.com/package/fn-wj-17

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install fn-wj-17`
- npm registry：https://registry.npmjs.org/fn-wj-17
