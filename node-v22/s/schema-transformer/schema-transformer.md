# schema-transformer

> 标签: JavaScript

## 简介

``` transformer     .object(lumine)     .select((lumine) => lumine.activity.is_online)     .mod((value) => Boolean(value))     .select((lumine) => lumine.is_allowed)     .mod((value) => Boolean(value))     .transform() ```

## 官网

- npm 页面：https://www.npmjs.com/package/schema-transformer

## 历史版本号

- 当前版本：0.0.2

- 0.0.2

## 获取地址

- npm 安装：`npm install schema-transformer`
- npm registry：https://registry.npmjs.org/schema-transformer
