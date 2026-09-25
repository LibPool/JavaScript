# db-conn-mysql

> 标签: JavaScript

## 简介

``` const config: MySqlConnectionConfig = { 	host: 'localhost', 	user: 'root', 	database: 'test', 	password:'*******' }; let conn = await driver.connect(config); let data = await conn.executeQuery("select 1 from dual"); await conn.close(); ```

## 官网

- 官网：https://gitee.com/sparklex/db-conn-mysql
- npm 页面：https://www.npmjs.com/package/db-conn-mysql

## 历史版本号

- 当前版本：1.6.1

- 0.0.1
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8
- 1.5.0
- 1.6.0
- 1.6.1

## 获取地址

- npm 安装：`npm install db-conn-mysql`
- npm registry：https://registry.npmjs.org/db-conn-mysql
