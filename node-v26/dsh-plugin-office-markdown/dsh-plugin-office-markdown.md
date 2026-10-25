# dsh-plugin-office-markdown

> 标签: batch-conversion, context-optimization, cordis, deepseek-harness, docx, dsh, dsh-bundle, dsh-plugin, markdown, markitdown, office, pdf, pptx, token-saving, xlsx

## 简介

DeepSeek Harness（DSH）bundle 插件：在模型读取工作区里的 Office / PDF 文件之前，用 Microsoft MarkItDown 自动把它们转成 Markdown，转换结果写在源文件旁边，因此进入上下文的只是一个 .md 路径。产物完整保留、绝不裁剪，同时返回字节数、行数、token 估算与标题结构索引，并给出「先看结构、再用 grep 定位」的读取策略；支持一次调用批量转换多个文件或整个目录。内置设置页可以检查本机的 Python 环境、按需一键配置或卸载 MarkI

## 官网

- 官网：https://github.com/Z8906/dsh-plugin-office-markdown#readme
- 源码仓库：git+https://github.com/Z8906/dsh-plugin-office-markdown.git
- npm 页面：https://www.npmjs.com/package/dsh-plugin-office-markdown

## 历史版本号

- 当前版本：1.2.4

- 1.2.1
- 1.2.2
- 1.2.3
- 1.2.4

## 获取地址

- npm 安装：`npm install dsh-plugin-office-markdown`
- npm registry：https://registry.npmjs.org/dsh-plugin-office-markdown
- Node 要求：>=18
