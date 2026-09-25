# @yuants/secret

> 标签: JavaScript

## 简介

`@yuants/secret` 是 Yuan 体系内的 secret 管理库，提供基于 Curve25519 公钥加密的分布式秘密存储和访问控制能力，适用于离线环境下的敏感数据持久化存储，允许提前指定读取者的 ED25519 公钥，并在读取者不在线的情况下完成非对称加密并持久化存储。而后，读取者可以在任何时间点使用其私钥解密获取秘密数据。

## 官网

- npm 页面：https://www.npmjs.com/package/@yuants/secret

## 历史版本号

- 当前版本：0.5.4

- 0.4.3
- 0.4.4
- 0.4.5
- 0.4.6
- 0.4.7
- 0.4.8
- 0.4.9
- 0.5.0
- 0.5.1
- 0.5.2
- 0.5.3
- 0.5.4
- 共 64 个版本，完整清单见 npm registry。

## 获取地址

- npm 安装：`npm install @yuants/secret`
- npm registry：https://registry.npmjs.org/@yuants/secret
