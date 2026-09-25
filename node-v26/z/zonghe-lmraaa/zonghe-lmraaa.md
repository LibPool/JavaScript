# zonghe-lmraaa

> 标签: JavaScript

## 简介

//1.封装函数 const copyFn = (add, del) => {     //2.判断起始文件是否存在 如果不存在则不能复制     if (!fs.existsSync(add)) {         throw new Error("源文件不存在" + add);         return;     }     //3.判断目标文件是否存在 如果存在则不能复制     if (fs.existsSync(del)) {         throw new Error

## 官网

- npm 页面：https://www.npmjs.com/package/zonghe-lmraaa

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install zonghe-lmraaa`
- npm registry：https://registry.npmjs.org/zonghe-lmraaa
