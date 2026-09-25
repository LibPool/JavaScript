# sippreep.extensions.versionchanges

> 标签: JavaScript

## 简介

展示两个同项目但不同版号的 Revit 模型（model A 及 model B）。在 Viewer 里，每个 Revit 构件都会对应到一个 dbId，而这个 dbId 也会对应到一个 Reivt 唯一码（Unique GUID），这个唯一码也是 Viewer 的外部编码（Extenal Id），所以只要在 model A 及 model B 里比对两者间有没有不存在的 Extenal Id，以及比对同一个 External Id 的构件属性里有没有被新增、修改及删除的参数，根据这个思路我们可以将没有修

## 官网

- npm 页面：https://www.npmjs.com/package/sippreep.extensions.versionchanges

## 历史版本号

- 当前版本：1.0.1

- 1.0.0
- 1.0.0-beta1
- 1.0.0-beta2
- 1.0.1
- 1.0.1-beta1

## 获取地址

- npm 安装：`npm install sippreep.extensions.versionchanges`
- npm registry：https://registry.npmjs.org/sippreep.extensions.versionchanges
