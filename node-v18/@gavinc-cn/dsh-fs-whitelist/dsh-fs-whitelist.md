# @gavinc-cn/dsh-fs-whitelist

> 标签: cordis, deepseek-harness, dsh, filesystem, plugin, sandbox

## 简介

顶替官方本地文件系统 provider：在官方工作区 + 临时区之外，把白名单目录（含自动学习白名单）也算作 write/edit 的可写根（trusted-code 的 fs fence，不是内核边界），让白名单目录的写入不再走「沙箱拒 → 带 sandbox_permissions 升权重试」。默认停用。

## 官网

- 官网：https://github.com/gavinc-cn/dsh-plugins/tree/master/packages/runtime/dsh-fs-whitelist#readme
- 源码仓库：git+https://github.com/gavinc-cn/dsh-plugins.git
- npm 页面：https://www.npmjs.com/package/@gavinc-cn/dsh-fs-whitelist

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.1

## 获取地址

- npm 安装：`npm install @gavinc-cn/dsh-fs-whitelist`
- npm registry：https://registry.npmjs.org/@gavinc-cn/dsh-fs-whitelist
