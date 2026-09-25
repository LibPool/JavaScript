# @near-snap/sdk

> 标签: JavaScript

## 简介

```ts async function main() {     const account = await NearSnapAccount.connect('mainnet')     const result = await account.executeTransaction({         receiverId: "herewallet.near",         actions: [{ type: 'Transfer', params: { deposit: '1' }}]     })

## 官网

- 官网：https://github.com/here-wallet/near-snap#readme
- 源码仓库：git+https://github.com/here-wallet/near-snap.git
- npm 页面：https://www.npmjs.com/package/@near-snap/sdk

## 历史版本号

- 当前版本：0.6.0

- 0.1.0
- 0.2.0
- 0.2.1
- 0.2.2
- 0.3.0
- 0.4.0
- 0.5.0
- 0.6.0

## 获取地址

- npm 安装：`npm install @near-snap/sdk`
- npm registry：https://registry.npmjs.org/@near-snap/sdk
