# claude-code-context-diet

> 标签: agent, anthropic, claude, claude-code, context, context-rot, hooks, mcp, token-optimization

## 简介

Claude Code hook that compresses tool outputs before they re-enter context. Fights the 1M-context degradation documented in claude-code#35296 by deduplicating Read results, stripping noise, and truncating oversize Bash outputs.

## 官网

- 官网：https://github.com/linkoinsight/claude-code-context-diet#readme
- 源码仓库：git+https://github.com/linkoinsight/claude-code-context-diet.git
- npm 页面：https://www.npmjs.com/package/claude-code-context-diet

## 历史版本号

- 当前版本：0.1.2

- 0.1.0
- 0.1.1
- 0.1.2

## 获取地址

- npm 安装：`npm install claude-code-context-diet`
- npm registry：https://registry.npmjs.org/claude-code-context-diet
- Node 要求：>=18
