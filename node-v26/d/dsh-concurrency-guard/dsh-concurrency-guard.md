# dsh-concurrency-guard

> 标签: concurrency, deepseek-harness, dsh-plugin, monitor, rate-limit, semaphore, webui-panel

## 简介

DSH 并发请求监控与门闩：挂钩 llm/stream 瀑布，统计全部在途模型请求并按来源分类（主会话/子代理/插件/压缩/标题）与会话活跃聚合，达到上限 FIFO 排队，防止并发超限被供应商锁号；v1.5.0 新增会话级并发控制——实时给在线活跃会话设置并发数（rootId 解析到顶层会话，含子代理），面板新页签「会话并发」；v1.5.1 异常明细改 tab 切换并新增「按分类×错误信息」汇总报表；v1.5.2 异常明细加「今日/全部」范围切换、逐条明细改倒序、新增历史数据清理（保留最近 N 天 / 分

## 官网

- 官网：https://github.com/fu827707013/dsh-concurrency-guard
- 源码仓库：git+https://github.com/fu827707013/dsh-concurrency-guard.git
- npm 页面：https://www.npmjs.com/package/dsh-concurrency-guard

## 历史版本号

- 当前版本：1.5.6

- 1.3.5
- 1.3.6
- 1.3.7
- 1.3.8
- 1.3.9
- 1.4.0
- 1.4.1
- 1.4.2
- 1.5.0
- 1.5.1
- 1.5.2
- 1.5.6

## 获取地址

- npm 安装：`npm install dsh-concurrency-guard`
- npm registry：https://registry.npmjs.org/dsh-concurrency-guard
- Node 要求：>=20
