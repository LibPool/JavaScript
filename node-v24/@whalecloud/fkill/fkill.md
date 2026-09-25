# @whalecloud/fkill

> 标签: die, exit, fkill, force, kill, killall, killing, proc, ps, sigkill, sigterm, taskkill, terminate, zap

## 简介

fork原因是我发现 node18-slim容器里，运行这个报错 因为没有ps这个命令，所以 `process-exists` 这个报根本无法运行。 所以删除相关的代码，以便支持在 node18-slim里运行

## 官网

- 官网：https://github.com/wangxh89/fkill#readme
- 源码仓库：git+https://github.com/wangxh89/fkill.git
- npm 页面：https://www.npmjs.com/package/@whalecloud/fkill

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install @whalecloud/fkill`
- npm registry：https://registry.npmjs.org/@whalecloud/fkill
- Node 要求：^12.20.0 || ^14.13.1 || >=16.0.0
