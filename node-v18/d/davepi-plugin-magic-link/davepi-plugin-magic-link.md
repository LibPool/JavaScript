# davepi-plugin-magic-link

> 标签: auth, davepi, davepi-plugin, email, invite, login, magic-link, passwordless

## 简介

Passwordless email magic-link login for dAvePi. Mounts /auth/magic-link/{request,verify,invite} routes, stores only SHA-256 token hashes in a TTL-indexed collection, sends links via the framework mailer, and issues the framework's standard JWT on verify.

## 官网

- 官网：https://docs.davepi.dev/features/plugins/
- 源码仓库：git+https://github.com/projik/davepi.git
- npm 页面：https://www.npmjs.com/package/davepi-plugin-magic-link

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install davepi-plugin-magic-link`
- npm registry：https://registry.npmjs.org/davepi-plugin-magic-link
- Node 要求：>=18
