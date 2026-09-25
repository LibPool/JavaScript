# utils-1902a-2

> 标签: JavaScript

## 简介

```javascript function copyDir(src, dest) {   // 代码实现   // 1.兼容处理   dest 不存在就创建   !fs.existsSync(dest) && fs.mkdirSync(dest)   // 2.读取src的子目录   fs.readdirSync(src).forEach(v => {     // 2-1 拼接路径     let midSrc = src + "/" + v     let midDest = de

## 官网

- npm 页面：https://www.npmjs.com/package/utils-1902a-2

## 历史版本号

- 当前版本：3.0.0

- 1.0.0
- 1.0.1
- 1.0.2
- 2.0.0
- 3.0.0

## 获取地址

- npm 安装：`npm install utils-1902a-2`
- npm registry：https://registry.npmjs.org/utils-1902a-2
