# @engine7/lancedb-intel

> 标签: JavaScript

## 简介

Intel Mac (darwin-x64) 专用的 lancedb 转发包。lancedb 从 0.23 起不再发布 macOS Intel 的原生二进制（该平台的包停在 0.22.3），所以 x64 Mac 上只能用老版本。os/cpu 字段让 npm 只在 darwin+x64 安装本包，其它平台完全跳过——这是 npm 唯一能表达「按平台选依赖版本」的机制（实测：file: 形式的本地依赖不认 os/cpu，必须发到 registry 才生效）。

## 官网

- 官网：https://github.com/ruiyangruiyi/engine7#readme
- 源码仓库：git+https://github.com/ruiyangruiyi/engine7.git
- npm 页面：https://www.npmjs.com/package/@engine7/lancedb-intel

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.1

## 获取地址

- npm 安装：`npm install @engine7/lancedb-intel`
- npm registry：https://registry.npmjs.org/@engine7/lancedb-intel
