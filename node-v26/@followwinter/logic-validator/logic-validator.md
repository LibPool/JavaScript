# @followwinter/logic-validator

> 标签: JavaScript

## 简介

逻辑表达式校验工具，(1|2)&amp;(2|3) ### 使用方式 - 正确 ```javascript let tokens = new LV.Tokenizer().tokenize('1&2') new LV.Analyst().analyse(tokens) // return ast ``` - 错误 ```javascript let tokens = new LV.Tokenizer().tokenize('(11') new LV.Analyst().analyse(tokens) //

## 官网

- npm 页面：https://www.npmjs.com/package/@followwinter/logic-validator

## 历史版本号

- 当前版本：1.1.5

- 1.1.0
- 1.1.1
- 1.1.2
- 1.1.3
- 1.1.4
- 1.1.5

## 获取地址

- npm 安装：`npm install @followwinter/logic-validator`
- npm registry：https://registry.npmjs.org/@followwinter/logic-validator
