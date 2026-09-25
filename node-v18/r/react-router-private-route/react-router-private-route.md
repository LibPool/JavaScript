# react-router-private-route

> 标签: JavaScript

## 简介

``` <Router>   <div>     <PrivateRoute path="/" auth={Math.random() > Math.random()} redirect={"/login"} component={loadable(() => import("./pages/home"))} />     <Route exact path="/login" component={loadable(() => import("./pages/login"))} />   </d

## 官网

- npm 页面：https://www.npmjs.com/package/react-router-private-route

## 历史版本号

- 当前版本：0.0.3

- 0.0.1
- 0.0.2
- 0.0.3

## 获取地址

- npm 安装：`npm install react-router-private-route`
- npm registry：https://registry.npmjs.org/react-router-private-route
