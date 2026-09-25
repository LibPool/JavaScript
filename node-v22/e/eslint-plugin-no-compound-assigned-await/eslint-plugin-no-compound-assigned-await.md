# eslint-plugin-no-compound-assigned-await

> 标签: eslint, eslint-plugin, eslintplugin

## 简介

`x += await y` means `x = x + await y`. The value of x is 'fixed' synchonously, and y is later added to it. This is hard to discern when reading the code, and generally unwanted.

## 官网

- 官网：https://github.com/PJWalker/eslint-plugin-no-compound-assigned-await#readme
- 源码仓库：git+https://github.com/PJWalker/eslint-plugin-no-compound-assigned-await.git
- npm 页面：https://www.npmjs.com/package/eslint-plugin-no-compound-assigned-await

## 历史版本号

- 当前版本：1.0.0

- 0.0.0
- 0.0.1
- 1.0.0

## 获取地址

- npm 安装：`npm install eslint-plugin-no-compound-assigned-await`
- npm registry：https://registry.npmjs.org/eslint-plugin-no-compound-assigned-await
- Node 要求：>=0.10.0
