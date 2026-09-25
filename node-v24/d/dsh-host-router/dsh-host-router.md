# dsh-host-router

> 标签: clash, cordis-plugin, deepseek, deepseek-harness, dispatcher, dsh, network, proxy, routing, sniff, undici

## 简介

dsh 外挂式网络路由:按 hostname 给 dsh 请求分流——勾选的域名走本地代理(Clash 等),其余直连。内置嗅探,自动扫描 dsh 访问过的 hostname,设置页勾选即生效(保存即热生效,免重启)。纯外挂:dependencies 空,运行时零 require,全靠宿主 ctx 注入;不碰 settings.yaml provider 配置。

## 官网

- npm 页面：https://www.npmjs.com/package/dsh-host-router

## 历史版本号

- 当前版本：0.1.8

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3
- 0.1.4
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.8

## 获取地址

- npm 安装：`npm install dsh-host-router`
- npm registry：https://registry.npmjs.org/dsh-host-router
- Node 要求：>=18
