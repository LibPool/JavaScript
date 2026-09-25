# dsh-remote-file-system

> 标签: deepseek-harness, dsh, dsh-plugin, edit, file, read, remote, ssh, write

## 简介

模型可见的远程文件工具 read_remote、write_remote、edit_remote，经 ssh 读写远程主机文件。write_remote 只允许新建，绝无覆写分支；文件后端 RemoteFileSystem 不继承 FileSystem，仅借用 @deepseek-ai/dsh-fs 的类型词表与 FsError。标准可安装的 dsh host 插件。

## 官网

- 官网：https://github.com/better-er/dsh-remote-file-system#readme
- 源码仓库：git+https://github.com/better-er/dsh-remote-file-system.git
- npm 页面：https://www.npmjs.com/package/dsh-remote-file-system

## 历史版本号

- 当前版本：0.1.0

- 0.0.1
- 0.1.0

## 获取地址

- npm 安装：`npm install dsh-remote-file-system`
- npm registry：https://registry.npmjs.org/dsh-remote-file-system
- Node 要求：>=26.3.1
