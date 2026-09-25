# kxco-pq-hsm

> 标签: argon2, fips-203, fips-204, hardware-security-module, hsm, key-management, key-protection, key-storage, kxco, luna, ml-dsa, ml-kem, nist, pkcs11, post-quantum, pqc, softhsm2, yubikey, zero-trust

## 简介

ML-DSA-65 and ML-KEM-768 key custody on a PKCS#11 HSM. Generates ML-DSA keys on the token with CKA_EXTRACTABLE=false and signs with C_Sign, so the private key never enters host memory. signingMode reports on-token only after a probe signature proves it.

## 官网

- 官网：https://kxco.ai
- 源码仓库：git+https://github.com/KnightsbridgeAIQ/kxco-pq-hsm.git
- npm 页面：https://www.npmjs.com/package/kxco-pq-hsm

## 历史版本号

- 当前版本：1.4.2

- 1.0.8
- 1.0.9
- 1.1.0
- 1.1.1
- 1.1.2
- 1.2.0
- 1.3.0
- 1.3.1
- 1.3.2
- 1.4.0
- 1.4.1
- 1.4.2

## 获取地址

- npm 安装：`npm install kxco-pq-hsm`
- npm registry：https://registry.npmjs.org/kxco-pq-hsm
- Node 要求：>=20.19
