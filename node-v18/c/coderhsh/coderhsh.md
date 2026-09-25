# coderhsh

> 标签: cli, coderhsh, hsh, 定制脚手架, 脚手架

## 简介

1.  配置好 package.json 中的 bin,把'hsh'改成自己定义的,这是脚手架的命令 2.  在当前项目的终端中输入 npm link,这行命令会自动读取 package.json 文件中的 bin 配置项,跟电脑的环境变量链接,这样才可以在终端中执行 bin 的命令 3.  如果需要创建命令只需要 2 步 1.在 lib/core/commands/create.js 下 initCommand 函数的 commandList 中添加命令以及参数 2.在 actions 文件中添加跟命令

## 官网

- 官网：https://github.com/coderhsh
- npm 页面：https://www.npmjs.com/package/coderhsh

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install coderhsh`
- npm registry：https://registry.npmjs.org/coderhsh
