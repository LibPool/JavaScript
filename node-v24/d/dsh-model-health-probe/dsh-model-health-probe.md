# dsh-model-health-probe

> 标签: anthropic-messages, auto-retry, connectivity-probe, deepseek-harness, default-model, dsh-plugin, model-health, model-health-probe, openai-completions, openai-responses, webui-panel

## 简介

DSH 模型健康检查：在会话视图新增「模型健康检查」页签，按「供应商(baseURL分组) → API类型 → 模型 → 路由」四行按钮选定目标，手动发送一条真实裸 HTTP 测试请求（支持 openai-completions / openai-responses / anthropic-messages 三协议，流式与非流式可切），一屏展示耗时、TTFT、HTTP 状态、token 用量、响应内容与三层诊断链（API请求 / 模型响应 / 严格校验），错误全部人话化。可把当前模型一键设为默认（下次打开

## 官网

- 官网：https://github.com/fu827707013/dsh-model-health-probe
- 源码仓库：git+https://github.com/fu827707013/dsh-model-health-probe.git
- npm 页面：https://www.npmjs.com/package/dsh-model-health-probe

## 历史版本号

- 当前版本：0.3.4

- 0.3.3
- 0.3.4

## 获取地址

- npm 安装：`npm install dsh-model-health-probe`
- npm registry：https://registry.npmjs.org/dsh-model-health-probe
- Node 要求：>=20
