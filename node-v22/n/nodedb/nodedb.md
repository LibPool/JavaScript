# nodedb

> 标签: JavaScript

## 简介

暂时想不到准确的描述方式，以后再 # 以下是一些笔记 - 这个“数据库”，目前能力有限，使用文件存储，而且是明文的，这个底层以后再想 - 每个“文档”存储一个文件，文件名为 md5(user_identity)+'_'+user_identity - 文件内容为json序列化，这个部分以后可能要注意try-catch - 导出的模块是个function，需要传入一个对象作为参数，对象包含一个属性 path，代表的是数据存储的位置，缺省是是当前目录 - 你要确保这个path有写入权限 - 模块

## 官网

- npm 页面：https://www.npmjs.com/package/nodedb

## 历史版本号

- 当前版本：0.0.16

- 0.0.11
- 0.0.12
- 0.0.13
- 0.0.14
- 0.0.15
- 0.0.16
- 0.0.3
- 0.0.4
- 0.0.5
- 0.0.6
- 0.0.7
- 0.0.8

## 获取地址

- npm 安装：`npm install nodedb`
- npm registry：https://registry.npmjs.org/nodedb
