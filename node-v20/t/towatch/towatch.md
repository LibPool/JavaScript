# towatch

> 标签: command, file change, watch

## 简介

如其名，监听文件或文件夹变化，变了就执行你想要执行的命令，就这么简单 # 怎么干 `npx towatch path=${your path base root} command='${your command}' -f` - path: 需要监听的文件（夹）路径，根据你项目根路径 - command: 你要执行的命令，一般使用单引号括起来避免冲突 - first: 是否在最开始调用命令，简写（-f） # 更新 - 1.0.2-0 会杀死上一个遗留的子进程 - 1.0.3-0 底层改用sp

## 官网

- npm 页面：https://www.npmjs.com/package/towatch

## 历史版本号

- 当前版本：1.0.5-0

- 1.0.0
- 1.0.1
- 1.0.2-0
- 1.0.3-0
- 1.0.4-0
- 1.0.5-0

## 获取地址

- npm 安装：`npm install towatch`
- npm registry：https://registry.npmjs.org/towatch
