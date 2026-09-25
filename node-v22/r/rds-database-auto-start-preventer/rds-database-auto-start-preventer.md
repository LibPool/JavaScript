# rds-database-auto-start-preventer

> 标签: aws, aws-cdk, cdk, rds

## 简介

CDK stack that stops RDS DB instances and clusters after they are auto-started by AWS (RDS-EVENT-0154 / RDS-EVENT-0153). It uses EventBridge rules and a Durable Lambda to detect auto-start events, optionally filter by tags, stop the resource if it matches

## 官网

- 官网：https://github.com/gammarers-aws-cdk-constructs/rds-database-auto-start-preventer#readme
- 源码仓库：git+https://github.com/gammarers-aws-cdk-constructs/rds-database-auto-start-preventer.git
- npm 页面：https://www.npmjs.com/package/rds-database-auto-start-preventer

## 历史版本号

- 当前版本：0.4.0

- 0.2.3
- 0.2.4
- 0.2.5
- 0.2.6
- 0.3.0
- 0.3.1
- 0.3.2
- 0.3.3
- 0.3.4
- 0.3.5
- 0.3.6
- 0.4.0

## 获取地址

- npm 安装：`npm install rds-database-auto-start-preventer`
- npm registry：https://registry.npmjs.org/rds-database-auto-start-preventer
- Node 要求：>= 20.0.0
