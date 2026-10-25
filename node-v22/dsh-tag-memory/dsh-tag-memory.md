# dsh-tag-memory

> 标签: agent-memory, csv, deepseek-harness, dsh-plugin, local-first, tag-memory

## 简介

DSH 插件：让智能体有一份自己的记忆库——一张只追加的 CSV，稳定读写，闲时能整理。每个智能体每轮自动拿到标签字典（systemPrompt.section，函数值），由模型判断该不该记、每维取什么值，并提供 memory_write / memory_recall 两个工具。界面上有条目表格、维度筛选、搜索导出，以及备份 / 恢复 / 合并。零依赖，全部落本地文件。安装时会探测各智能体的 MEMORY.md 并写入一段受控说明（标记块、幂等、块外一个字节不碰、挂载自愈）。

## 官网

- 官网：https://github.com/marsma-101/dsh-tag-memory#readme
- 源码仓库：git+https://github.com/marsma-101/dsh-tag-memory.git
- npm 页面：https://www.npmjs.com/package/dsh-tag-memory

## 历史版本号

- 当前版本：0.3.1

- 0.0.0-stage
- 0.3.0
- 0.3.1

## 获取地址

- npm 安装：`npm install dsh-tag-memory`
- npm registry：https://registry.npmjs.org/dsh-tag-memory
