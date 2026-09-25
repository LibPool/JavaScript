# @lidaxi/prompt-enhance

> 标签: deepseek-harness, dsh, llm, plugin, prompt, prompt-enhance

## 简介

提示词增强（DSH 通用插件）：三种模式（基础/标准/专家）读取会话工作区项目上下文并调用 LLM 增强输入框提示词，支持结果对比确认、采用后撤回、失败模型回退链、按模型能力自动适配推理档位（网关不支持时自动去参重试）、待确认问答闭环（逐条回答后带答案重新增强）、组合行 config 可配置、可取消。Host 半提供 /api/prompt-enhance/enhance；浏览器半在 composer 工具行注册模式选择与 ✦ 按钮、对比面板与忙碌状态卡。随 harness 启动自动加载，无需手动重新加载

## 官网

- 官网：https://github.com/sunzhentao/dsh--prompt--enhance
- 源码仓库：git+https://github.com/sunzhentao/dsh--prompt--enhance.git
- npm 页面：https://www.npmjs.com/package/@lidaxi/prompt-enhance

## 历史版本号

- 当前版本：1.5.0

- 1.3.0
- 1.3.1
- 1.3.2
- 1.3.3
- 1.4.0
- 1.5.0

## 获取地址

- npm 安装：`npm install @lidaxi/prompt-enhance`
- npm registry：https://registry.npmjs.org/@lidaxi/prompt-enhance
- Node 要求：>=22
