# lsd

> 标签: directory stream, list directory, ls, ls stream, lsd

## 简介

wait what? this isn't that type of program. Streaming ls like module. Write a path into lsd and get back a stream of that directories contents. You will get back a stream of full paths. You can easily hookup a filtering transform stream to alter the output to fit your needs (i.e. strip the paths if you don't need them). Initialize lsd with depth option and then write a path to lsd and get back a stream of the directories contents DEPTH levels deep. Pass 0 to depth option and get back the entire directory tree.

## 官网

- 源码仓库：https://github.com/swys/lsd.git
- npm 页面：https://www.npmjs.com/package/lsd

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install lsd`
- npm registry：https://registry.npmjs.org/lsd
