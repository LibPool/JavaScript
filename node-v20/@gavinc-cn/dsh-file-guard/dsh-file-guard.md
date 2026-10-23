# @gavinc-cn/dsh-file-guard

> 标签: JavaScript

## 简介

会话文件守卫插件: 每轮收尾 (agent/turn-stopping) 比对「本会话写下的文件」与磁盘, 发现被外部进程/并行会话/文件同步覆盖或回退时 steer 一条简短提示 (不自动改回); 状态格式与 kimi 侧 file_guard.py 双向兼容, 并附带等价 CLI (note/check/report/restore/ack/forget/stop-hook)。

## 官网

- 官网：https://github.com/gavinc-cn/dsh-plugins/tree/master/packages/runtime/dsh-file-guard#readme
- 源码仓库：git+https://github.com/gavinc-cn/dsh-plugins.git
- npm 页面：https://www.npmjs.com/package/@gavinc-cn/dsh-file-guard

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @gavinc-cn/dsh-file-guard`
- npm registry：https://registry.npmjs.org/@gavinc-cn/dsh-file-guard
