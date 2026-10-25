# @gavinc-cn/dsh-sandbox-whitelist

> 标签: cordis, deepseek-harness, dsh, landlock, plugin, sandbox

## 简介

在官方本地沙箱 provider 之上补「白名单根 = 执行层可写根」：项目根 + 白名单目录 + 临时区可写、其余只读（Linux bwrap/Landlock；Windows 用官方 windows-acl 受限令牌 + 写 SID ACE），让命令级闸门的判定落到执行层。默认停用。

## 官网

- 官网：https://github.com/gavinc-cn/dsh-plugins/tree/master/packages/runtime/dsh-sandbox-whitelist#readme
- 源码仓库：git+https://github.com/gavinc-cn/dsh-plugins.git
- npm 页面：https://www.npmjs.com/package/@gavinc-cn/dsh-sandbox-whitelist

## 历史版本号

- 当前版本：0.2.0

- 0.0.0-stage
- 0.2.0

## 获取地址

- npm 安装：`npm install @gavinc-cn/dsh-sandbox-whitelist`
- npm registry：https://registry.npmjs.org/@gavinc-cn/dsh-sandbox-whitelist
