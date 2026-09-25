# atom-obvervable

> 标签: JavaScript

## 简介

Atom contains a value which can change over time. ```js interface Atom<T, A: mixed[]> {   deref(): T,   reset(value: T): Atom<T>,   swap(fn: (currentValue: T, ...args:A) => T, ...args: A): Atom<T>,   watch(fn: (newValue: T, oldValue: T) => void): () => vo

## 官网

- 官网：https://github.com/igorDolzh/js-atom#readme
- 源码仓库：git+https://github.com/igorDolzh/js-atom.git
- npm 页面：https://www.npmjs.com/package/atom-obvervable

## 历史版本号

- 当前版本：0.1.0

- 0.1.0

## 获取地址

- npm 安装：`npm install atom-obvervable`
- npm registry：https://registry.npmjs.org/atom-obvervable
