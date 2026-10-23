# @kxreas/dsh-plugin-backpack

> 标签: backup, deepseek-harness, dsh, dsh-plugin, export, import, migration, plugin

## 简介

插件背包（Plugin Backpack）：在「设置 → 插件背包」里记录并导出当前 DSH 插件（不含本插件）。导出四选一：完整插件包 zip、TGZ 混合包（npm 来源只写清单、非 npm 来源附带物理包）、带 SHA-256 校验的文本清单、压缩口令；清单/口令会提示非 npm 来源不能带源码。支持添加导入与全量替换导入，全量替换需输入「我确定」并自动备份，安装失败只记录一次、结束后弹窗汇总，失败自动回滚；仅非 npm 的部分包会被禁止用于全量替换。

## 官网

- npm 页面：https://www.npmjs.com/package/@kxreas/dsh-plugin-backpack

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @kxreas/dsh-plugin-backpack`
- npm registry：https://registry.npmjs.org/@kxreas/dsh-plugin-backpack
- Node 要求：^22.19.0 || >=24.0.0
