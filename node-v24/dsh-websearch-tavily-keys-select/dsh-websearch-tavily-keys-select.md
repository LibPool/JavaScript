# dsh-websearch-tavily-keys-select

> 标签: cordis, deepseek-harness, dsh, dsh-plugin, plugin, search, tavily, tencent-cloud, web-search, yuanbao

## 简介

DSH 的 Web 搜索链路：源 → key → 额度 三级模型。一个源可放多把 key（每把独立额度、可单独启停/删除），源有自己的计费方式；key 额度用完自动换同源下一把，整源不可用再换下一个源。内置腾讯元宝搜索（SearchPro，额度闸门 + Freshness/Site 意图解析）、Tavily（credits 记账 + 查额度）、DeepSeek 搜索 API。

## 官网

- 官网：https://github.com/apherchin/dsh-websearch-tavily-keys-select#readme
- 源码仓库：git+https://github.com/apherchin/dsh-websearch-tavily-keys-select.git
- npm 页面：https://www.npmjs.com/package/dsh-websearch-tavily-keys-select

## 历史版本号

- 当前版本：3.0.0

- 2.0.0
- 3.0.0

## 获取地址

- npm 安装：`npm install dsh-websearch-tavily-keys-select`
- npm registry：https://registry.npmjs.org/dsh-websearch-tavily-keys-select
- Node 要求：>=20
