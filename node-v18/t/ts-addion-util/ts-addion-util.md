# ts-addion-util

> 标签: JavaScript

## 简介

```bash # 1. 构建产物 (确保 dist/ 已生成) # 1.1 prebuild: 调用 generateExports 脚本，递归生成模组的 index.ts，无需手动编辑 （如果有错请更正） # 1.2 rollup.config.ts 进一步处理dist下的结构。esm, cjs下是各个模组压缩有的js（暂定都是index.min.js），并在顶层目录下生成index.min.js统一导出所有模组，***同时也对应package.json的exports对象配置*** # 1.

## 官网

- npm 页面：https://www.npmjs.com/package/ts-addion-util

## 历史版本号

- 当前版本：0.0.6

- 0.0.1
- 0.0.2
- 0.0.3
- 0.0.4
- 0.0.5
- 0.0.6

## 获取地址

- npm 安装：`npm install ts-addion-util`
- npm registry：https://registry.npmjs.org/ts-addion-util
