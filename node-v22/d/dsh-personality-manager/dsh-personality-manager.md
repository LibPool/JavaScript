# dsh-personality-manager

> 标签: cordis, deepseek, dsh, harness, mentor, persona, personality, plugin, tutor

## 简介

DeepSeek Harness (dsh) 插件：Personality 容器与双路径人格注入器。主路径经系统提示词 section 注入(官方预设)；经 systemPrompt.layers 注册表探测 complete persona(v1.1.1 修复:瀑布后裁剪导致的误判)，确认 section 必被裁剪时自动回退为 source.kind='skill-invocation' 的请求级消息穿透 allowKinds 门控。保守检测确保任一预设下只走一条路径，无重复注入。输入栏 Persona

## 官网

- npm 页面：https://www.npmjs.com/package/dsh-personality-manager

## 历史版本号

- 当前版本：1.1.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.1.0
- 1.1.1
- 1.1.2
- 1.1.3

## 获取地址

- npm 安装：`npm install dsh-personality-manager`
- npm registry：https://registry.npmjs.org/dsh-personality-manager
- Node 要求：>=22
