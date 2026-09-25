# svgaplayerweb-iosfix

> 标签: JavaScript

## 简介

手机端H5项目引用该仓库时，IOS端存在问题，XMLHttpRequest报错。 分析发现，IOS端会将本地文件转换为file:///......路径文件，安卓端为https://......路径文件，代码调用XMLHttpRequest转换文件为arrayBuffer格式，IOS因协议 问题报错。 因此本仓库做出调整，兼容IOS系统文件格式转换，详细步骤如下： 1. 先使用[工具](https://www.bejson.com/ui/file_to_base64/)将svga文件转换为base6

## 官网

- 官网：https://github.com/JGX19/SVGAPlayer-Web-FixIOS#readme
- 源码仓库：git+https://github.com/JGX19/SVGAPlayer-Web-FixIOS.git
- npm 页面：https://www.npmjs.com/package/svgaplayerweb-iosfix

## 历史版本号

- 当前版本：1.0.2

- 0.0.1
- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install svgaplayerweb-iosfix`
- npm registry：https://registry.npmjs.org/svgaplayerweb-iosfix
