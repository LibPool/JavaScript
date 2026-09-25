# ec2-instance-running-scheduler

> 标签: cdk, durable, ec2, execution, lambda, scheduler, slack

## 简介

AWS CDK construct library that starts and stops EC2 instances on a cron schedule using EventBridge Scheduler and a Durable Execution Lambda. The handler discovers instances with the Resource Groups Tagging API, issues start/stop, waits until each instance

## 官网

- 官网：https://github.com/gammarers-aws-cdk-constructs/ec2-instance-running-scheduler#readme
- 源码仓库：git+https://github.com/gammarers-aws-cdk-constructs/ec2-instance-running-scheduler.git
- npm 页面：https://www.npmjs.com/package/ec2-instance-running-scheduler

## 历史版本号

- 当前版本：0.4.5

- 0.3.1
- 0.3.2
- 0.3.3
- 0.3.4
- 0.3.5
- 0.3.6
- 0.4.0
- 0.4.1
- 0.4.2
- 0.4.3
- 0.4.4
- 0.4.5

## 获取地址

- npm 安装：`npm install ec2-instance-running-scheduler`
- npm registry：https://registry.npmjs.org/ec2-instance-running-scheduler
- Node 要求：>= 20.0.0
