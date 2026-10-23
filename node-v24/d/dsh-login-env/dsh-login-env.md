# dsh-login-env

> 标签: cordis, dsh, dsh-plugin, environment, login-shell, path

## 简介

让 DSH 的 shell 工具继承登录 shell 的环境：启动时解析一次登录 shell（~/.zprofile 里的 brew shellenv 等），写回 PATH，使 gh / node / pnpm 等命令在从 Dock 启动 DSH 时同样可用。

## 官网

- 源码仓库：git+https://github.com/LC-86/dsh-plugins.git
- npm 页面：https://www.npmjs.com/package/dsh-login-env

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-login-env`
- npm registry：https://registry.npmjs.org/dsh-login-env
- Node 要求：^22.19.0 || >=24.0.0
