# @huo15/huo15-openclaw-enhance

> 标签: agent, enhance, memory, openclaw, plugin, safety

## 简介

火一五·克劳德·龙虾增强插件 v6.7.16 — bot-upload-link error path 漏判 hotfix：v6.7.15 本地实测三轮（直连/远程全链路/中途中断），前两轮完美，但第三轮发现 req.on('error') / ws.on('error') 触发后 Promise done，外面 `if (aborted)` 不拦截 error case 继续走 renameSync(partial, file) → ENOENT 误报 stderr（partial 已被 rmSync

## 官网

- 源码仓库：https://cnb.cool/huo15/ai/huo15-openclaw-enhance
- npm 页面：https://www.npmjs.com/package/@huo15/huo15-openclaw-enhance

## 历史版本号

- 当前版本：6.7.24

- 6.7.20
- 6.7.21
- 6.7.22
- 6.7.23
- 6.7.24
- 6.7.3
- 6.7.4
- 6.7.5
- 6.7.6
- 6.7.7
- 6.7.8
- 6.7.9

## 获取地址

- npm 安装：`npm install @huo15/huo15-openclaw-enhance`
- npm registry：https://registry.npmjs.org/@huo15/huo15-openclaw-enhance
