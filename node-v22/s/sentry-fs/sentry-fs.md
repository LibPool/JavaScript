# sentry-fs

> 标签: JavaScript

## 简介

> Sentry-fs是一个用于接收数据上传的任务节点, 当初始化一个上传任务后, 可以根据实际的传输需要, 分批进行数据片段的发送, 当最后数据包的累计字节数等于任务初始化时设定的总字节数时上传任务即完成, 数据片段将合并生成并保存为一个完整的文件. 目前上传可支持http1.1/https/http2/socket/socket.io/websocket/ftp/amqp/mqtt等协议;  > > 上传的文件通过MD5唯一标识, 如果开通了下载插件(useDLoader), 则可通过MD5作为参数下

## 官网

- npm 页面：https://www.npmjs.com/package/sentry-fs

## 历史版本号

- 当前版本：0.0.2

- 0.0.1
- 0.0.2

## 获取地址

- npm 安装：`npm install sentry-fs`
- npm registry：https://registry.npmjs.org/sentry-fs
