# dsh-users-open-source-workspace

> 标签: deepseek-harness, dsh, dsh-plugin, explorer, open-folder, workspace

## 简介

dsh-users-open-source 的伴生包：受理 POST /dsh-users-open-source/open-workspace，在系统文件管理器里打开用户当前工作区目录（设置页「开源用户」里那颗「云端备份」按钮）。目录只从 DSH 自己的工作区账本里取，客户端只能递 sessionId；Windows 上用包内 PowerShell 脚本打开并显形（DSH 以隐藏方式启动子进程，直接 spawn explorer.exe 只会得到一个 visible=false 的隐身窗口）。它不是独立

## 官网

- 官网：https://github.com/KAIROSLLL/dsh-users-open-source#readme
- 源码仓库：git+https://github.com/KAIROSLLL/dsh-users-open-source.git
- npm 页面：https://www.npmjs.com/package/dsh-users-open-source-workspace

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-users-open-source-workspace`
- npm registry：https://registry.npmjs.org/dsh-users-open-source-workspace
- Node 要求：>=22.13.0
