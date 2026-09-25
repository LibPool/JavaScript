# dsh-peak-block

> 标签: deepseek, deepseek-harness, dsh, dsh-plugin, official, peak-hours, provider, rate-limit, routing

## 简介

梁文峰时间拦截官方 DeepSeek API 请求：北京时间工作日高峰时段 09:00-12:00、14:00-18:00，中国法定节假日全天谷价不拦截，自动拦截发往官方 provider `deepseek-official` 的模型请求，可切换到第三方中转或预留的本机转 API 端口，未配置则阻止并提示；非高峰不拦、正常走官方，专治高峰掉速与刷屏。标准可安装 dsh 插件，host 单半身，设置经 cordis 配置文件注入。

## 官网

- 官网：https://github.com/better-er/dsh-peak-block#readme
- 源码仓库：git+https://github.com/better-er/dsh-peak-block.git
- npm 页面：https://www.npmjs.com/package/dsh-peak-block

## 历史版本号

- 当前版本：0.2.1

- 0.1.0
- 0.1.1
- 0.2.0
- 0.2.1

## 获取地址

- npm 安装：`npm install dsh-peak-block`
- npm registry：https://registry.npmjs.org/dsh-peak-block
