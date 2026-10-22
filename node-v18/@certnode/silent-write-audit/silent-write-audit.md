# @certnode/silent-write-audit

> 标签: audit, orm, phantom-column, postgrest, pre-commit, prisma, schema-drift, silent-fail, static-analysis, stripe, supabase, webhook

## 简介

Static-analysis audit for phantom-column / phantom-field references in Supabase/PostgREST writes and Prisma client calls. Catches the silent-fail bug class where .update({...}) with a non-existent column drops the entire statement without error.

## 官网

- 官网：https://github.com/srbryant86/silent-write-audit#readme
- 源码仓库：git+https://github.com/srbryant86/silent-write-audit.git
- npm 页面：https://www.npmjs.com/package/@certnode/silent-write-audit

## 历史版本号

- 当前版本：0.3.1

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3
- 0.3.0
- 0.3.1

## 获取地址

- npm 安装：`npm install @certnode/silent-write-audit`
- npm registry：https://registry.npmjs.org/@certnode/silent-write-audit
- Node 要求：>=18
