# @hwfee/dsh-genui

> 标签: deepseek, deepseek-harness, dsh, dsh-plugin, generative-ui, intelligent-ui, react, skill

## 简介

DeepSeek Harness 的生成式 UI 插件：模型用 render_ui 工具直接写一段 React 代码，回答里就地渲染成一张可交互卡片，而不是只给文字。附带一个内置 skill，教模型什么时候值得用界面、什么时候一段话就够。代码在独立的 sandboxed iframe 里执行：opaque origin，读不到宿主 DOM、存储和 cookie，CSP 阻断 fetch/XHR/WebSocket；卡片要发消息必须由用户点确认。 / Generative UI for DeepSeek H

## 官网

- npm 页面：https://www.npmjs.com/package/@hwfee/dsh-genui

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install @hwfee/dsh-genui`
- npm registry：https://registry.npmjs.org/@hwfee/dsh-genui
- Node 要求：^22.19.0 || >=24.0.0
