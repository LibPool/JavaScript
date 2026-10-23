# @xiciyang/training-pretrain

> 标签: deepseek-harness, dsh, dsh-plugin

## 简介

继续预训练（continued pretraining）薄插件：领域语料校验（双轨去泄漏 + 全量 PII）→ 公共训练循环（training-core，容器内 transformers）→ 分片续训（步号与数据位置连续性机器可验）→ 合并 → serving 部署 → 遗忘门禁。依赖长任务 1 冻结的六个 @ai-infra/* 共享库。

## 官网

- 官网：https://github.com/xiciyang/training-pretrain#readme
- 源码仓库：git+https://github.com/xiciyang/training-pretrain.git
- npm 页面：https://www.npmjs.com/package/@xiciyang/training-pretrain

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @xiciyang/training-pretrain`
- npm registry：https://registry.npmjs.org/@xiciyang/training-pretrain
