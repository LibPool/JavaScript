# @mafesoftware/outbox

> 标签: correo, drizzle, multi-tenant, outbox, whatsapp

## 简介

Outbox transaccional para correo y WhatsApp: la app encola un mensaje en la MISMA transacción que el hecho de negocio (encolar, exige transacción) y un cron lo procesa con reintentos, backoff con jitter y FOR UPDATE SKIP LOCKED (procesarOutbox). decidir/b

## 官网

- 官网：https://github.com/mafesoftware/paquetes#readme
- 源码仓库：git+https://github.com/mafesoftware/paquetes.git
- npm 页面：https://www.npmjs.com/package/@mafesoftware/outbox

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @mafesoftware/outbox`
- npm registry：https://registry.npmjs.org/@mafesoftware/outbox
- Node 要求：>=20
