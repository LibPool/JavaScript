# server-validator-nocobase

> 标签: JavaScript

## 简介

nocobase 项目中afterStart事件中添加，如下所示 ``` app.on("afterStart", () => {   const validators = [{     collectionName: 'posts',     fieldValidators:[{       type: "string",       name: "email",       validate: { isEmail: true },     }]   }];   updateValidators(app

## 官网

- 官网：https://github.com/pangff/server-validator-nocobase#readme
- 源码仓库：git+https://github.com/pangff/server-validator-nocobase.git
- npm 页面：https://www.npmjs.com/package/server-validator-nocobase

## 历史版本号

- 当前版本：1.0.7

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7

## 获取地址

- npm 安装：`npm install server-validator-nocobase`
- npm registry：https://registry.npmjs.org/server-validator-nocobase
