# dsh-sensitive-replace

> 标签: blocklist, content-exists-risk, cordis, cordis-plugin, deepseek-harness, dsh, dsh-plugin, plugin, sensitive-words

## 简介

敏感字符自动替换：按用户维护的 YAML 屏蔽表（全局 / 按 Provider ID / 模型，默认 $DSH_HOME/sensitive-blocklist.yaml）在内容进入会话上下文前替换命中字符，规避 DeepSeek 官方 Content Exists Risk 400（v0.7.2：状态行显示屏蔽表是否存在；屏蔽表缺失时自动建空表 + 形态告警 + 规则级命中计数；兼容 DSH 0.2.0-rc.x）

## 官网

- 官网：https://github.com/Short-Arm-Ape/dsh-sensitive-replace#readme
- 源码仓库：git+https://github.com/Short-Arm-Ape/dsh-sensitive-replace.git
- npm 页面：https://www.npmjs.com/package/dsh-sensitive-replace

## 历史版本号

- 当前版本：0.7.2

- 0.0.0-stage
- 0.7.1
- 0.7.2

## 获取地址

- npm 安装：`npm install dsh-sensitive-replace`
- npm registry：https://registry.npmjs.org/dsh-sensitive-replace
- Node 要求：>=20
