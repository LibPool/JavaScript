# statebox-monitor

> 标签: JavaScript

## 简介

```js const conn = new Connection("ws://localhost:3011"); await conn.connect(); const monitor = new Monitor(conn, "My test job monitor"); const job = monitor.createJob("new job"); job.log("test log"); job.isDone = true; ```

## 官网

- 官网：https://github.com/rzseattle/statebox#readme
- 源码仓库：git+https://github.com/rzseattle/statebox.git
- npm 页面：https://www.npmjs.com/package/statebox-monitor

## 历史版本号

- 当前版本：0.0.13

- 0.0.1-alpha.49
- 0.0.1-alpha.50
- 0.0.1-alpha.52
- 0.0.11
- 0.0.12
- 0.0.13
- 0.0.2
- 0.0.3
- 0.0.4
- 0.0.5
- 0.0.7
- 0.0.9

## 获取地址

- npm 安装：`npm install statebox-monitor`
- npm registry：https://registry.npmjs.org/statebox-monitor
- Node 要求：>=14.15.3
