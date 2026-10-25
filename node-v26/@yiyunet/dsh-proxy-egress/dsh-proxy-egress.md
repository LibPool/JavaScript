# @yiyunet/dsh-proxy-egress

> 标签: connect-tunnel, deepseek-harness, dsh, dsh-plugin, egress, fail-closed, http-proxy, proxy, settings-panel

## 简介

本地出口代理（egress）桥：把只接受无凭据 HTTP(S) 代理地址的消费方，接到需要账号密码的上游代理上。失败即断联，绝不改走直连。零构建、零运行时依赖。 Local egress proxy bridge for DSH: hand a credential-free proxy URL to consumers that reject credentials, and inject the upstream auth on the hop that needs it. Fail-closed:

## 官网

- 官网：https://github.com/yiyunet/dsh-proxy-egress#readme
- 源码仓库：git+https://github.com/yiyunet/dsh-proxy-egress.git
- npm 页面：https://www.npmjs.com/package/@yiyunet/dsh-proxy-egress

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @yiyunet/dsh-proxy-egress`
- npm registry：https://registry.npmjs.org/@yiyunet/dsh-proxy-egress
- Node 要求：>=22.19
