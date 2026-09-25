# pomelo-protobuf

> 标签: JavaScript

## 简介

Protobuf protocol is a high efficient binary protocol for data encode, this module implement the protobuf protocol, and used in [pomelo](https://github.com/NetEase/pomelo) for data transfer. Of course, pomelo-protobuf can also be used independently in other projects. ##Architecture Unlike the google protobuf, we provide a universal encoder and decoder in pomelo-protobuf. We use protos file as meta data to encode/decode messages, so you do not need to add any code to your project, instead , what you need is to add a protos.json (or two for different encoder and decoder messages) files to define the message need to encode by protobuf.The architecture of pomelo-protobuf is as follow:

## 官网

- npm 页面：https://www.npmjs.com/package/pomelo-protobuf

## 历史版本号

- 当前版本：0.4.0

- 0.1.0
- 0.3.0
- 0.3.1
- 0.3.2
- 0.3.3
- 0.3.4
- 0.3.5
- 0.4.0

## 获取地址

- npm 安装：`npm install pomelo-protobuf`
- npm registry：https://registry.npmjs.org/pomelo-protobuf
