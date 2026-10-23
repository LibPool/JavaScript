# dsh-tool-content-guard

> 标签: 422, content, cordis, deepseek-harness, dsh, dsh-plugin, guard, post-execute, session, text, tools, 工具兜底

## 简介

DSH 插件：host 侧兜底——把工具 content 里非字符串的 `text` 强制字符串化（默认），或在开发模式下直接把这次调用判失败。挂在官方扩展点 tools/post-execute，先让其它策略跑完再归一化，避免 `{"type":"text","text":[…]}` 这种非法块把 DeepSeek Messages 请求打成 422（invalid type: sequence, expected a string），也避免它落进会话日志、毒掉整个会话。

## 官网

- 官网：https://gitee.com/hc905/dsh-tool-content-guard
- 源码仓库：git+https://gitee.com/hc905/dsh-tool-content-guard.git
- npm 页面：https://www.npmjs.com/package/dsh-tool-content-guard

## 历史版本号

- 当前版本：1.0.3

- 0.0.0-stage
- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install dsh-tool-content-guard`
- npm registry：https://registry.npmjs.org/dsh-tool-content-guard
