# @feiyang666/dsh-vault

> 标签: backup, chat-history, cordis, data-safety, deepseek, dsh, restore, vault

## 简介

数据保险箱：为 DeepSeek Harness 提供备份、清空检测与一键恢复。备份触发时机：启动备份、意外关闭备份、手动备份（不再按会话落盘或定时全量备份，避免大量任务运行时卡死）。自动备份 ~/.dsh 的聊天记录(sessions)、工作区数据(storages)、设置(settings.yaml)、凭据与 profile 配置到用户主目录 ~/.dsh-backups（最多保留 10 份）；若已安装用量插件（dsh-usage-plugin），其用量数据（usage-records.json /

## 官网

- 官网：https://github.com/feiyang-dev/dsh-vault#readme
- 源码仓库：git+https://github.com/feiyang-dev/dsh-vault.git
- npm 页面：https://www.npmjs.com/package/@feiyang666/dsh-vault

## 历史版本号

- 当前版本：1.5.0

- 1.3.0
- 1.3.1
- 1.3.2
- 1.3.3
- 1.5.0

## 获取地址

- npm 安装：`npm install @feiyang666/dsh-vault`
- npm registry：https://registry.npmjs.org/@feiyang666/dsh-vault
- Node 要求：>=18
