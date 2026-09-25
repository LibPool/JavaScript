# run-at-fps

> 标签: JavaScript

## 简介

```js import {runAtFps} from 'run-at-fps'; let runner = runAtFps(60); let i = 0; let stop = runner(() => {     i++;     i > 10 && stop();     // code here, call 10 times at 60fps. }); ```

## 官网

- npm 页面：https://www.npmjs.com/package/run-at-fps

## 历史版本号

- 当前版本：0.0.1

- 0.0.1

## 获取地址

- npm 安装：`npm install run-at-fps`
- npm registry：https://registry.npmjs.org/run-at-fps
