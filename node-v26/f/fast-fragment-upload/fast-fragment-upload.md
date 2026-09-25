# fast-fragment-upload

> 标签: JavaScript

## 简介

> WIP: 一个简单使用并且快速的分片上传封装函数，使用 Worker 进行分片上传，Worker 开启数量根据 CPU 内核数控制，支持多个文件同时上传，每片默认按照 5MB 进行分片，可自己设置。另外提供了 2 个函数，fragmentUpload 会在单个文件全部分完片后依次回调，fragmentUpload1 则是在每分好一个片立即回调，可按照具体需求使用。

## 官网

- 官网：https://github.com/Simon-He95/fast-fragment-upload#readme
- 源码仓库：git+https://github.com/Simon-He95/fast-fragment-upload.git
- npm 页面：https://www.npmjs.com/package/fast-fragment-upload

## 历史版本号

- 当前版本：0.0.6

- 0.0.0
- 0.0.1
- 0.0.2
- 0.0.3
- 0.0.4
- 0.0.5
- 0.0.6

## 获取地址

- npm 安装：`npm install fast-fragment-upload`
- npm registry：https://registry.npmjs.org/fast-fragment-upload
