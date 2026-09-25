# monofile

> 标签: JavaScript

## 简介

export MONOFILE="$0"; cat "$0" | awk '/\<a name\=\"2\.1\.\"\>/{y=1;next}y' | tail -n+3 | bash -euo pipefail -- /dev/stdin "$@"; exit 0 -->

## 官网

- npm 页面：https://www.npmjs.com/package/monofile

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install monofile`
- npm registry：https://registry.npmjs.org/monofile
