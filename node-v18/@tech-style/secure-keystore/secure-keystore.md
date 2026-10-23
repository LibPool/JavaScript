# @tech-style/secure-keystore

> 标签: aes-256-gcm, api-keys, authenticated-encryption, ci-cd, cli, config, configuration, credentials, decrypt, devops, dotenv, encrypt, encryption, encryption-at-rest, env, environment-variables, key-store, keystore, nodejs, pbkdf2, secret-management, secrets, typescript, vault, zero-dependencies

## 简介

Encrypted secrets at rest for Node.js, with no service to run. Two-layer AES-256-GCM encryption over PBKDF2-SHA256: a user key unlocks a per-store master key, and the master key unlocks each value under its own salt. Zero dependencies, a CLI, and stateles

## 官网

- 官网：https://tech-style.co/product-secure-keystore.html
- 源码仓库：git+https://github.com/eharain/secure-keystore.git
- npm 页面：https://www.npmjs.com/package/@tech-style/secure-keystore

## 历史版本号

- 当前版本：3.0.0

- 0.0.0-stage
- 3.0.0

## 获取地址

- npm 安装：`npm install @tech-style/secure-keystore`
- npm registry：https://registry.npmjs.org/@tech-style/secure-keystore
- Node 要求：>=18.0.0
