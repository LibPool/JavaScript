# dsh-plugin-billing-card

> 标签: billing, cost, deepseek, deepseek-harness, dsh, dsh-plugin, token, usage

## 简介

计费卡片：在输入框下方实时统计当前会话各模型的 token 用量，并按可配置的价格表（默认 DeepSeek 官方峰谷价，CNY/USD）估算费用；同时统计 DeepSeek 官方网页搜索 / 抓取 API 的调用次数与按次费用（Search 服务端调用免费至 2026-11-01 00:00，之后按每 1000 次 5 元估算）。Host 端注册 billingUsage 会话投影（纯函数、可重放），Client 端是输入框下方的药丸与明细卡片；价格表、峰谷规则和搜索计价可通过插件配置扩展以支持其他模型

## 官网

- 官网：https://github.com/tofu-zyc/dsh-plugin-tofu-box/tree/main/dsh-plugin-billing-card
- 源码仓库：git+https://github.com/tofu-zyc/dsh-plugin-tofu-box.git
- npm 页面：https://www.npmjs.com/package/dsh-plugin-billing-card

## 历史版本号

- 当前版本：0.2.0

- 0.0.0-stage
- 0.1.0
- 0.2.0

## 获取地址

- npm 安装：`npm install dsh-plugin-billing-card`
- npm registry：https://registry.npmjs.org/dsh-plugin-billing-card
