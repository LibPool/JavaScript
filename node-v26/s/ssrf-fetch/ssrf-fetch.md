# ssrf-fetch

> 标签: dns-rebinding, fetch, metadata, security, ssrf, toctou, undici, url, webhook

## 简介

A drop-in fetch() that blocks SSRF: refuses loopback/private/link-local/CGNAT targets and pins the connection to the validated IP to defeat DNS rebinding (TOCTOU).

## 官网

- 官网：https://github.com/iansduncan-oss/ssrf-fetch#readme
- 源码仓库：git+https://github.com/iansduncan-oss/ssrf-fetch.git
- npm 页面：https://www.npmjs.com/package/ssrf-fetch

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install ssrf-fetch`
- npm registry：https://registry.npmjs.org/ssrf-fetch
- Node 要求：>=20
