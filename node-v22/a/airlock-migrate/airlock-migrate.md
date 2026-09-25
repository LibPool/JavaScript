# airlock-migrate

> 标签: ci, ci-gate, github-action, linter, migration, postgres, rls, row-level-security, security, supabase

## 简介

The CI gate for dangerous Supabase/Postgres migrations. Fails your build when a migration ships a table without RLS, disables RLS, or adds a USING (true) policy, and warns on a dropped policy/trigger. No database connection required.

## 官网

- 官网：https://shipsealed.com
- 源码仓库：git+https://github.com/mateuszingano/airlock-migrate.git
- npm 页面：https://www.npmjs.com/package/airlock-migrate

## 历史版本号

- 当前版本：0.2.0

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3
- 0.1.4
- 0.1.5
- 0.2.0

## 获取地址

- npm 安装：`npm install airlock-migrate`
- npm registry：https://registry.npmjs.org/airlock-migrate
- Node 要求：>=18
