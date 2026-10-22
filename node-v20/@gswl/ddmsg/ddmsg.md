# @gswl/ddmsg

> 标签: JavaScript

## 简介

``` sendDDMsg("https://oapi.dingtalk.com/robot/send?access_token=xxxxx", {     msgtype: MsgType.text,     text: {     content: "我的消息",     },     at: { isAtAll: true }, }) .then((v) => {     console.log(v); }) .catch((e) => {     console.log(e); }); ```

## 官网

- npm 页面：https://www.npmjs.com/package/@gswl/ddmsg

## 历史版本号

- 当前版本：1.0.1

- 1.0.1

## 获取地址

- npm 安装：`npm install @gswl/ddmsg`
- npm registry：https://registry.npmjs.org/@gswl/ddmsg
