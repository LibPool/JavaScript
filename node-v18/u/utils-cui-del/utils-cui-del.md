# utils-cui-del

> 标签: JavaScript

## 简介

```javascript function copydir(dir, newdir) {     !fs.existsSync(newdir) && fs.mkdirSync(newdir);     fs.readFileSync(dir).forEach(item => {         let dirname = dir + '/' + item;         let newdirName = newdir + '/' + item;         if (fs.statSyn

## 官网

- npm 页面：https://www.npmjs.com/package/utils-cui-del

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install utils-cui-del`
- npm registry：https://registry.npmjs.org/utils-cui-del
