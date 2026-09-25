# egg-qr-log

> 标签: JavaScript

## 简介

```js   // app.js    async didReady() {       this.app.httpclient.on('request', (req) => {         // 可以在这里设置一些 trace headers，方便全链路跟踪         req.args.headers = transHeader(req.ctx, req.args.headers || {})       })   }   ```

## 官网

- npm 页面：https://www.npmjs.com/package/egg-qr-log

## 历史版本号

- 当前版本：1.0.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install egg-qr-log`
- npm registry：https://registry.npmjs.org/egg-qr-log
