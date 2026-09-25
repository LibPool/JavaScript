# resolve-array-overrides

> 标签: JavaScript

## 简介

var resolveArrayOverrides = require("resolve-array-overrides")     var DNA = require("organic").DNA     var dna = new DNA({       "default": {         "value": [1, 2, 3, 4]       },       "mode": {         "default": {           "value": [{ "$unshift": 0 }, { "$push": 5 }]         }       }     })     resolveArrayOverrides(dna, "mode")     expect(dna.default.value[0]).toBe(0)     expect(dna.default.value[5]).toBe(5) // 0, 1, 2, 3, 4, 5

## 官网

- 官网：https://github.com/outbounder/resolve-array-overrides
- 源码仓库：git://github.com/outbounder/resolve-array-overrides.git
- npm 页面：https://www.npmjs.com/package/resolve-array-overrides

## 历史版本号

- 当前版本：0.0.1

- 0.0.0
- 0.0.1

## 获取地址

- npm 安装：`npm install resolve-array-overrides`
- npm registry：https://registry.npmjs.org/resolve-array-overrides
