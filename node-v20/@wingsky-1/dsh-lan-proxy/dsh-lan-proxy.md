# @wingsky-1/dsh-lan-proxy

> 标签: deepseek-harness, dsh, lan, plugin, proxy, tunnel

## 简介

局域网访问 dsh web UI：在 0.0.0.0:<port> 监听，把 HTTP/HTTPS 与 WebSocket/wss 转发到回环 web 服务器（默认 127.0.0.1:3080）。重写 Host/Origin 以通过 /api 浏览器信任围栏，仅接受 IP 字面量或 localhost 的 Host 头（DNS 重绑定防护）。HTTPS 默认并存（3443），证书可配置或自动生成自签名。

## 官网

- 源码仓库：https://github.com/wingsky-1/dsh-plugin-hub.git
- npm 页面：https://www.npmjs.com/package/@wingsky-1/dsh-lan-proxy

## 历史版本号

- 当前版本：0.2.5

- 0.1.4
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.8
- 0.1.9
- 0.2.0
- 0.2.1
- 0.2.2
- 0.2.3
- 0.2.4
- 0.2.5

## 获取地址

- npm 安装：`npm install @wingsky-1/dsh-lan-proxy`
- npm registry：https://registry.npmjs.org/@wingsky-1/dsh-lan-proxy
- Node 要求：>=20.0.0
