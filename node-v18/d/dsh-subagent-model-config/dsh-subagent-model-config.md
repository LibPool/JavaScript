# dsh-subagent-model-config

> 标签: JavaScript

## 简介

可视化配置编队队员（Team teammate）的模型与推理档位 + 视频预设下的队员侧能力限制：运行时包装 subagents.startContinuable + agentTeams.spawnTeammate，不改官方任何文件、可逆、可一键关闭；对视频队员名加硬闸门（未命中规则即拒绝启动，执行模型必须人工点名可控）；当父会话 preset 为 video 时，对子代理注入 persona（遮蔽主窗身份卡）与 toolFilter.allow（视频解析工具白名单，fail-closed；团队通信工具

## 官网

- npm 页面：https://www.npmjs.com/package/dsh-subagent-model-config

## 历史版本号

- 当前版本：0.3.1

- 0.0.0-stage
- 0.3.0
- 0.3.1

## 获取地址

- npm 安装：`npm install dsh-subagent-model-config`
- npm registry：https://registry.npmjs.org/dsh-subagent-model-config
- Node 要求：>=22.0.0
