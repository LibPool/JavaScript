# @ponury/xml-object-stream

> 标签: JavaScript

## 简介

```javascript const xos = new XMLObjectStream(fs.createReadStream('books-catalog.xml'), {emitElements:['book']}); xos.on('end', function () {     // xml parsed }); xos.on('error', (err) => {     // handle error }); xos.on('element', (elm) => {     // do s

## 官网

- 官网：https://github.com/etk-pl/xml-object-stream#readme
- 源码仓库：git+https://github.com/etk-pl/xml-object-stream.git
- npm 页面：https://www.npmjs.com/package/@ponury/xml-object-stream

## 历史版本号

- 当前版本：0.2.0

- 0.2.0

## 获取地址

- npm 安装：`npm install @ponury/xml-object-stream`
- npm registry：https://registry.npmjs.org/@ponury/xml-object-stream
