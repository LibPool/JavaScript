# gzip-stream

> 标签: JavaScript

## 简介

To create a valid gzip from many individual streams first use createDeflatePart() which returns a through stream to convert your parts to the deflated part. when this through stream emits the 'end' event you should call its `metadata()` function which wil

## 官网

- 官网：https://github.com/balena-io-modules/gzip-stream
- 源码仓库：git+https://github.com/balena-io-modules/gzip-stream.git
- npm 页面：https://www.npmjs.com/package/gzip-stream

## 历史版本号

- 当前版本：2.1.0

- 2.0.0-build-support-node-18-3a5a9d6209d72760554344f96507b3d2b06c953d-1
- 2.0.1
- 2.0.1-build-add-npm-oidc-permissions-57efafa12587a346d77df74b99131c7f1df087d5-1
- 2.0.2
- 2.0.2-build-large-file-support-3b05fe923bd50846612f0954a840b06d7b07234a-1
- 2.0.2-build-large-file-support-9828ba3f6708000e1c8f0bf108d00fe2ba754dbf-1
- 2.0.2-build-large-file-support-a32d1f119b9779e041d981ae051b6e0f85eb0dba-1
- 2.0.2-build-large-file-support-f187e1a94e5c63f472b1fd52ca3a8ad858a3e8a5-1
- 2.0.3
- 2.0.3-build-update-crc-utils-7afa168fe3e497f0d2dae3f4f691faa6ea34c7bf-1
- 2.1.0
- 2.1.0-build-getGzipSizeFromParts-c6ded05785cb8c02c7eda1e429946270dc619782-1

## 获取地址

- npm 安装：`npm install gzip-stream`
- npm registry：https://registry.npmjs.org/gzip-stream
- Node 要求：>=16
