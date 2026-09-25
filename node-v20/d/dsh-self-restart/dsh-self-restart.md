# dsh-self-restart

> 标签: auto-refresh, cordis, deepseek-harness, dsh, plugin, restart

## 简介

DSH 自助重启：把「提权计划任务强杀进程树→端口释放确认→拉起服务」固化为插件能力；agent 或本机脚本一键调度重启，前端断线自动探测、服务恢复后自动刷新页面——让重启对用户近乎无感。v0.3.0 零登记自动发现：重启前扫描进行中任务写入账本，重启后错峰自动续跑。v0.3.4 业务门防自激：会话最后一次业务输入晚于其上次自动唤醒才登记，终结「已完成任务被反复唤醒自检」的连环空转。loopback 围栏防远程误触。

## 官网

- 官网：https://github.com/jiang12345-code/dsh-self-restart#readme
- 源码仓库：git+https://github.com/jiang12345-code/dsh-self-restart.git
- npm 页面：https://www.npmjs.com/package/dsh-self-restart

## 历史版本号

- 当前版本：0.3.4

- 0.3.4

## 获取地址

- npm 安装：`npm install dsh-self-restart`
- npm registry：https://registry.npmjs.org/dsh-self-restart
