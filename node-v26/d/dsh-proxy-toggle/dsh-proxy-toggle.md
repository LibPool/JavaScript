# dsh-proxy-toggle

> 标签: deepseek-harness, dsh, dsh-plugin, proxy, proxy-routing, toggle

## 简介

DSH 代理路由快捷开关：把主进程通过全局 fetch 发出的模型 API / Files API 请求在「直连」与「本地 HTTP/SOCKS5 代理」之间按请求即时切换；显式指定 dispatcher 的 web-fetch-http 固定出口不受此开关影响。默认复用 DSH 宿主认证；独立回环 fallback 端点、token/session 和 CLI 控制需通过 enableFallback=true 显式开启。GUI 悬浮按钮、可选全局热键和系统通知，状态持久化在 $DSH_HOME/vpn

## 官网

- 官网：https://github.com/APPLe-DF/dsh-proxy-toggle#readme
- 源码仓库：git+https://github.com/APPLe-DF/dsh-proxy-toggle.git
- npm 页面：https://www.npmjs.com/package/dsh-proxy-toggle

## 历史版本号

- 当前版本：0.1.3

- 0.1.2
- 0.1.3

## 获取地址

- npm 安装：`npm install dsh-proxy-toggle`
- npm registry：https://registry.npmjs.org/dsh-proxy-toggle
- Node 要求：>=22.19.0
