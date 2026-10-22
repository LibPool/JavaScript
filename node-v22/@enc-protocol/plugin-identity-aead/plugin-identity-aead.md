# @enc-protocol/plugin-identity-aead

> 标签: core, public

## 简介

IdentityAeadCryptoFn: spec-compliant single-owner deterministic confidentiality for Personal-enclave private content. content_key = HKDF-SHA256(identity_priv, salt=∅, 'enc-personal-private:'||enclave_id, 32) + XChaCha20-Poly1305 (24-byte nonce), sourced f

## 官网

- npm 页面：https://www.npmjs.com/package/@enc-protocol/plugin-identity-aead

## 历史版本号

- 当前版本：0.9.0

- 0.9.0

## 获取地址

- npm 安装：`npm install @enc-protocol/plugin-identity-aead`
- npm registry：https://registry.npmjs.org/@enc-protocol/plugin-identity-aead
- Node 要求：>=20
