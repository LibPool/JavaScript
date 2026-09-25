# toolgovern-integration-langgraph

> 标签: agent-security, ai-agents, langchain, langgraph, langgraphjs, runtime-governance, tool-calling, toolgovern

## 简介

Route LangGraph.js tool calls through toolgovern's governTool() gate before they reach ToolNode -- wraps each tool with the classifier, then re-wraps it with LangChain's own tool() factory so it slots into new ToolNode([...]) unchanged.

## 官网

- 官网：https://github.com/RudrenduPaul/toolgovern#readme
- 源码仓库：git+https://github.com/RudrenduPaul/toolgovern.git
- npm 页面：https://www.npmjs.com/package/toolgovern-integration-langgraph

## 历史版本号

- 当前版本：0.1.3

- 0.1.0
- 0.1.1
- 0.1.2
- 0.1.3

## 获取地址

- npm 安装：`npm install toolgovern-integration-langgraph`
- npm registry：https://registry.npmjs.org/toolgovern-integration-langgraph
