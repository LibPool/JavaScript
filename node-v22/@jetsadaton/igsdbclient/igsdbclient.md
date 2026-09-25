# @jetsadaton/igsdbclient

> 标签: JavaScript

## 简介

```typescript     const instant = new MSSqlConnect(     process.env.JWT as string,     'mssql',     'development',     'TEST CLIENT'   );     const res = await instant.query<{ ID: number }>({       sql: `SELECT ISNULL(max(id),0) + 1 as id from ERPDB.KPDBA

## 官网

- npm 页面：https://www.npmjs.com/package/@jetsadaton/igsdbclient

## 历史版本号

- 当前版本：1.2.5

- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.1.0
- 1.2.0
- 1.2.1
- 1.2.2
- 1.2.3
- 1.2.4
- 1.2.5

## 获取地址

- npm 安装：`npm install @jetsadaton/igsdbclient`
- npm registry：https://registry.npmjs.org/@jetsadaton/igsdbclient
