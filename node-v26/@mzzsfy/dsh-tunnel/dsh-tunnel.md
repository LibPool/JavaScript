# @mzzsfy/dsh-tunnel

> 标签: JavaScript

## 简介

路径穿透隧道:在 dsh 宿主进程内把 /p/<name> 反向代理到本地 TCP 端口(HTTP strip 转发 + 声明式 WS upgrade + 3xx Location 单头改写),支持 <name>.* 子域名全路径透传(任意 WS 路径);GUI 看板手动管理隧道,设置页独立配置节与侧边栏注入开关;向 ai 注册 tunnel_open/tunnel_list/tunnel_close 工具且「允许 ai 使用」可开关(关闭即注销);代理逻辑全在插件进程内,不引入 nginx/caddy

## 官网

- 官网：https://github.com/mzzsfy/dsh-plugin#readme
- 源码仓库：git+https://github.com/mzzsfy/dsh-plugin.git
- npm 页面：https://www.npmjs.com/package/@mzzsfy/dsh-tunnel

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @mzzsfy/dsh-tunnel`
- npm registry：https://registry.npmjs.org/@mzzsfy/dsh-tunnel
- Node 要求：>=22
