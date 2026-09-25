# dsh-privmask

> 标签: cordis, deepseek-harness, desensitization, dsh, llm, pii, plugin, privacy, redaction, 脱敏, 隐私保护

## 简介

DeepSeek Harness 本地脱敏插件：在 llm/stream 出口拦截发往云端大模型的请求，将密钥、PII、中文实体（姓名/身份证/公司/机关/地址等）替换为占位符后再发送；用户输入与工具结果在写入本地会话日志前同样遮罩，模型回复经入站还原以原值落盘与显示。

## 官网

- 官网：https://github.com/JunyuZhan/dsh-privmask#readme
- 源码仓库：git+https://github.com/JunyuZhan/dsh-privmask.git
- npm 页面：https://www.npmjs.com/package/dsh-privmask

## 历史版本号

- 当前版本：0.2.45

- 0.2.33
- 0.2.4
- 0.2.40
- 0.2.41
- 0.2.43
- 0.2.44
- 0.2.45
- 0.2.5
- 0.2.6
- 0.2.7
- 0.2.8
- 0.2.9

## 获取地址

- npm 安装：`npm install dsh-privmask`
- npm registry：https://registry.npmjs.org/dsh-privmask
- Node 要求：>=18
