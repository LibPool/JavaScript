# @3-/s3dist

> 标签: JavaScript

## 简介

```psql -- 清空表 DO $$ DECLARE     r RECORD; begin     FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP         EXECUTE 'DROP TABLE IF EXISTS public.' || quote_ident(r.tablename) || ' CASCADE';     END LOOP; END $$;

## 官网

- 官网：https://atomgit.com/i18n/lib/tree/dev/s3dist
- 源码仓库：git+https://atomgit.com/i18n/lib.git
- npm 页面：https://www.npmjs.com/package/@3-/s3dist

## 历史版本号

- 当前版本：0.2.1

- 0.1.10
- 0.1.3
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.8
- 0.1.9
- 0.2.1

## 获取地址

- npm 安装：`npm install @3-/s3dist`
- npm registry：https://registry.npmjs.org/@3-/s3dist
