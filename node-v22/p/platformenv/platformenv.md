# platformenv

> 标签: JavaScript

## 简介

This is a microlibrary with a single function `platformenv.define(global)`, that sets a number of predicates on the global object:`isNodeJs`, `isDevServer`, `isTesting`, and maybe more in the future.

Mainly used with solapp apps.

Include as: `require("platformenv").define global if typeof isNodeJs != "boolean"` in coffeescript, to make sure it is optimised away in uglifyjs.
(The whole reason to have a library that sets properties on the global object is that they can be optimised away, including dead code removal, by uglifyjs when they are defined by the preprocessor).

## 官网

- 源码仓库：http://github.com/rasmuserik/platformenv.git
- npm 页面：https://www.npmjs.com/package/platformenv

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install platformenv`
- npm registry：https://registry.npmjs.org/platformenv
