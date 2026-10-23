# @xiciyang/training-qat

> 标签: deepseek-harness, dsh, dsh-plugin

## 简介

QAT 薄插件：语料 O1 去泄漏 → 公共单体训练循环（training-core，容器内 torchao QAT 假量化）→ 对 QAT 训练后的权重施加真实的 INT8 量化（仓库自己的 llmcompressor INT8，compressed-tensors 产出）→ serving 部署 + 双门禁 + 跨插件对账。依赖长任务 1 冻结的六个 @ai-infra/* 共享库。

## 官网

- 官网：https://github.com/xiciyang/training-qat#readme
- 源码仓库：git+https://github.com/xiciyang/training-qat.git
- npm 页面：https://www.npmjs.com/package/@xiciyang/training-qat

## 历史版本号

- 当前版本：0.1.0

- 0.0.0-stage
- 0.1.0

## 获取地址

- npm 安装：`npm install @xiciyang/training-qat`
- npm registry：https://registry.npmjs.org/@xiciyang/training-qat
