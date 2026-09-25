# pwuploadimg

> 标签: JavaScript

## 简介

<!-- 上传图片 -->     // 1获取前端传来的信息     const stream = await ctx.getFileStream()     const {id}=stream.fields     // 2创建一个随机的文件名称      const fileName = Date.now() + path.extname(stream.filename).toLocaleLowerCase()     // 3创建一个文件夹保存地址     const address

## 官网

- npm 页面：https://www.npmjs.com/package/pwuploadimg

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install pwuploadimg`
- npm registry：https://registry.npmjs.org/pwuploadimg
