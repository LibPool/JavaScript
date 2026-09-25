# @emilte/named-routes

> 标签: nesting, path, paths, react, route, router, routes, scope, typescript, url, urls

## 简介

Example: ```ts const ROUTES = {    foo: include('/foo/', {      bar: 'bar/',      scope: include('scope/:param', { // <- Note the missing trailing slash.        baz: 'baz', // <- Note the missing trailing slash.        qux: 'qux/'      })    }) } ```

## 官网

- 官网：https://github.com/emilte/named-routes#readme
- 源码仓库：git+https://github.com/emilte/named-routes.git
- npm 页面：https://www.npmjs.com/package/@emilte/named-routes

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install @emilte/named-routes`
- npm registry：https://registry.npmjs.org/@emilte/named-routes
