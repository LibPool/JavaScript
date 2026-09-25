# msunc-cli

> 标签: msunc-cli, react, vue2

## 简介

这是用来编写指令和处理命令行的，具体用法如下： ```js const program = require("commander"); // 定义指令 program   .version('0.0.1')   .command('init', 'Generate a new project from a template')   .action(() => {     // 回调函数   }) // 解析命令行参数 program.parse(process.argv); ``` 回忆一下我们用过的 v

## 官网

- npm 页面：https://www.npmjs.com/package/msunc-cli

## 历史版本号

- 当前版本：1.0.5

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.4
- 1.0.5

## 获取地址

- npm 安装：`npm install msunc-cli`
- npm registry：https://registry.npmjs.org/msunc-cli
