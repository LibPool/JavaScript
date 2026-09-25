# @wingsky-1/dsh-mcp-manager

> 标签: deepseek-harness, dsh, mcp, model-context-protocol, plugin

## 简介

DSH MCP 管理器：Web 侧边栏「MCP」入口，面板按状态分级展示 MCP 服务器（运行中/连接中/已配置/失败），支持快速接入（stdio / streamable-http 表单）与粘贴 mcpServers JSON 导入。已连接服务器的工具一律经中间层工具（ws_mcp_search / ws_mcp_detail / ws_mcp_call / ws_mcp_list）访问：宿主注册名 mcp__<id>__<tool> 是内部标识（id 按 (工作空间, 服务器名) 分配、不可由服务器名

## 官网

- 源码仓库：https://github.com/wingsky-1/dsh-plugin-hub.git
- npm 页面：https://www.npmjs.com/package/@wingsky-1/dsh-mcp-manager

## 历史版本号

- 当前版本：0.2.5

- 0.1.4
- 0.1.5
- 0.1.6
- 0.1.7
- 0.1.8
- 0.1.9
- 0.2.0
- 0.2.1
- 0.2.2
- 0.2.3
- 0.2.4
- 0.2.5

## 获取地址

- npm 安装：`npm install @wingsky-1/dsh-mcp-manager`
- npm registry：https://registry.npmjs.org/@wingsky-1/dsh-mcp-manager
- Node 要求：>=20.0.0
