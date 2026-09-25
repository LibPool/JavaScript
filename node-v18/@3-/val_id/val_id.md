# @3-/val_id

> 标签: JavaScript

## 简介

``` CREATE TABLE IF NOT EXISTS `txt` ( `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT, `hash` binary(32) NOT NULL, `val` longtext DEFAULT NULL, PRIMARY KEY (`id`) /*T![clustered_index] CLUSTERED */, UNIQUE KEY `hash` (`hash`) ); ```

## 官网

- 官网：https://atomgit.com/i18n/lib/tree/dev/txt_id
- 源码仓库：git+https://atomgit.com/i18n/lib.git
- npm 页面：https://www.npmjs.com/package/@3-/val_id

## 历史版本号

- 当前版本：0.1.1

- 0.1.1

## 获取地址

- npm 安装：`npm install @3-/val_id`
- npm registry：https://registry.npmjs.org/@3-/val_id
