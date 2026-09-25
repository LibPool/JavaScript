# dsh-check-for-updates

> 标签: deepseek, dsh, dsh-plugin, harness, update, updater, version-check

## 简介

DSH 更新检查插件（静态 bundle）：首次打开自动检查 DSH 新版本（取 npm 实际最高版本），左下方弹窗提示并支持一键安排更新；采用分离式两阶段更新器（退出 DSH 后由独立进程完成安装，避免 Windows 运行中原地升级导致 koffi 断链），安装后做退出码/对盘/koffi 三重校验并支持断链自愈与一键修复；UI 使用 DSH 语义化主题 token；DSH 安装根/版本、node/npm 均在运行时探测，无硬编码路径。

## 官网

- 官网：https://github.com/ShanHaiFish/dsh-check-for-updates#readme
- 源码仓库：git+https://github.com/ShanHaiFish/dsh-check-for-updates.git
- npm 页面：https://www.npmjs.com/package/dsh-check-for-updates

## 历史版本号

- 当前版本：1.13.3

- 1.12.0
- 1.13.0
- 1.13.1
- 1.13.2
- 1.13.3

## 获取地址

- npm 安装：`npm install dsh-check-for-updates`
- npm registry：https://registry.npmjs.org/dsh-check-for-updates
