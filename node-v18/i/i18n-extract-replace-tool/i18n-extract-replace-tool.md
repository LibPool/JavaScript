# i18n-extract-replace-tool

> 标签: ast, i18n, vue-i18n, webpack

## 简介

基于vue-i18n国际化插件的的配套提取替换工具，不用修改源代码的前提下，充分保证项目内容语义的完整性和准确性。 ### 功能 - 抽取项目中的所有的中文词汇 - 将抽取词汇转换成vue-i18n插件支持的翻译函数 - 在构建过程中将翻译函数替换回源代码处 ### 特点 - 支持各种格式的代码，零改动成本 - 对包含变量的拼接字符串整段抽取，保证了语义和语序 - 在构建时进行多语言翻译函数替换，零侵入性 - 项目运行自动检索词汇，没有额外繁琐指令 - 内置opencc工具，一键进行繁体翻译 ### 拼接

## 官网

- npm 页面：https://www.npmjs.com/package/i18n-extract-replace-tool

## 历史版本号

- 当前版本：1.10.0

- 1.0.0
- 1.1.0
- 1.10.0
- 1.2.0
- 1.3.0
- 1.4.0
- 1.5.0
- 1.6.0
- 1.7.0
- 1.8.0
- 1.9.0

## 获取地址

- npm 安装：`npm install i18n-extract-replace-tool`
- npm registry：https://registry.npmjs.org/i18n-extract-replace-tool
