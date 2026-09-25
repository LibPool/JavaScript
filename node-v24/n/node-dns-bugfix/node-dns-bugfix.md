# node-dns-bugfix

> 标签: JavaScript

## 简介

Patch for NodeJS bug where calling `dns.setServers` during `dns.resolve*` being in progress causes Node process to crash with:  ``` node: ../deps/cares/src/ares_destroy.c:102: ares__destroy_servers_state: Assertion `ares__is_list_empty(&server->queries_to

## 官网

- 官网：https://github.com/dzek69/node-dns-bugfix#readme
- 源码仓库：git+https://github.com/dzek69/node-dns-bugfix.git
- npm 页面：https://www.npmjs.com/package/node-dns-bugfix

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install node-dns-bugfix`
- npm registry：https://registry.npmjs.org/node-dns-bugfix
