# @molejs/global-helper

> 标签: JavaScript

## 简介

```  /**    * 获取BSGlobal中值    */   getBSGlobal(key: string, defaultV?: any) {     return BSGlobal[key] || defaultV;   },   /**    * 获取租户信息    */   getTenantInfo(key?: string) {     return this.getBSGlobal(key || 'tenantInfo');   },   /**    * 获取用户信息    */

## 官网

- npm 页面：https://www.npmjs.com/package/@molejs/global-helper

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install @molejs/global-helper`
- npm registry：https://registry.npmjs.org/@molejs/global-helper
- Node 要求：>=6.0.0
