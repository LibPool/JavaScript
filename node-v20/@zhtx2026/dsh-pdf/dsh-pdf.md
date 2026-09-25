# @zhtx2026/dsh-pdf

> 标签: agent-tool, deepseek-harness, dsh, dsh-plugin, pdf, pdfjs, plugin

## 简介

DSH PDF 解析插件: 为 agent 提供 pdf_info / pdf_extract_text / pdf_render_page 三个工具。基于 pdfjs-dist + @napi-rs/canvas; 对未内嵌字体的 PDF (如嘉立创EDA导出) 自动改用系统字体渲染文字。热插拔 — 通过 cordis.patch.yml + profile node_modules 软链接挂载, 无需改动 dsh 源码。

## 官网

- 官网：https://github.com/zhtx2024/dsh-pdf#readme
- 源码仓库：git+https://github.com/zhtx2024/dsh-pdf.git
- npm 页面：https://www.npmjs.com/package/@zhtx2026/dsh-pdf

## 历史版本号

- 当前版本：0.1.1

- 0.1.1

## 获取地址

- npm 安装：`npm install @zhtx2026/dsh-pdf`
- npm registry：https://registry.npmjs.org/@zhtx2026/dsh-pdf
- Node 要求：^22.19.0 || >=24.0.0
