# @hivelocity/formify

> 标签: JavaScript

## 简介

``` const LoginForm = Formify({ first: '', last: '', contacts: [{ first: 'Barney', last: 'Calhoun' }] }, ({error, fields}) => ( <> <Error message={error} /> <TextField {...fields.first} /> <TextField {...fields.last} type="password" /> {fields.contacts &&

## 官网

- npm 页面：https://www.npmjs.com/package/@hivelocity/formify

## 历史版本号

- 当前版本：0.0.6

- 0.0.5
- 0.0.6

## 获取地址

- npm 安装：`npm install @hivelocity/formify`
- npm registry：https://registry.npmjs.org/@hivelocity/formify
