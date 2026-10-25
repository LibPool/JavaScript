# @kkabuka/dsh-agent-notify

> 标签: deepseek, dsh, dsh-plugin, harness, notification, notify, toast, web, windows

## 简介

DSH Web GUI 任务完成/需你输入通知（维护中的 fork，适配 dsh 0.2.x）：agent 完成任务或需要你输入/批准时弹出 Windows 系统级通知，点气泡跳回该会话。相对上游 1.0.0：① 点击跳转改接 ctx.uiWorkspace.openSession ② 需输入信号改接 ctx.uiSession.sessionStatus ③ 卡片三枚失效令牌改为内核实有令牌 ④ 通知正文摘要改接 ctx.uiConversation（替换已删的 SessionSnapshot.node

## 官网

- 官网：https://github.com/chidaic/dsh-agent-notify
- 源码仓库：git+https://github.com/chidaic/dsh-agent-notify.git
- npm 页面：https://www.npmjs.com/package/@kkabuka/dsh-agent-notify

## 历史版本号

- 当前版本：1.0.3

- 0.0.0-stage
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install @kkabuka/dsh-agent-notify`
- npm registry：https://registry.npmjs.org/@kkabuka/dsh-agent-notify
