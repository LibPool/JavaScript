# dome03

> 标签: JavaScript

## 简介

```js const copyDir = (usedDir, targetDir) => {         // 创建目标文件         fs.mkdirSync(targetDir);         // 判断是否有要拷贝的文件         if (!fs.existsSync(usedDir)) {             // 如果没有   抛出错误             throw new Error('不存在要拷贝的文件' + usedDir);

## 官网

- npm 页面：https://www.npmjs.com/package/dome03

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install dome03`
- npm registry：https://registry.npmjs.org/dome03
