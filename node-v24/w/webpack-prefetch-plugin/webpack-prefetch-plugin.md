# webpack-prefetch-plugin

> 标签: dns-prefetch, prefetch, webpack

## 简介

根据路由 path 进行命名。页面文件打包构建后，会生成 js、css、map 文件，可以过滤掉 map 文件，生成路由 path 和 js、css 文件路径的映射关系。最后组装成 script 脚本，注入 HTML 文件里。页面加载后，就可以根据页面的路由 path，找出对应要加载的 js、css 资源。如果知道用户将要去什么页面，就可以预加载对应页面资源了。如果用户要去的是第三方页面，会进行 DNS 预解析流程。

## 官网

- npm 页面：https://www.npmjs.com/package/webpack-prefetch-plugin

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install webpack-prefetch-plugin`
- npm registry：https://registry.npmjs.org/webpack-prefetch-plugin
