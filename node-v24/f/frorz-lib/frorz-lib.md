# frorz-lib

> 标签: JavaScript

## 简介

## external 该字段用于说明那些依赖是我们不想打入到最终的包里面的, 外部的包。通常我们会放到`peerDependence`或者`dependence`中。 - `dependence` - 中的依赖在用户使用我们的包的时候，会自动直接下载到我们包的node_modules中 - `peerDependence` - 则是要求用户要安装这个依赖。在安装我们包的过程中，如果用户没有次依赖，则会提示用户自行下载。比如组件库会将 vue, react等设置peerDependence

## 官网

- 官网：https://github.com/frorz1/utils#readme
- 源码仓库：git+https://github.com/frorz1/utils.git
- npm 页面：https://www.npmjs.com/package/frorz-lib

## 历史版本号

- 当前版本：1.0.3

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3

## 获取地址

- npm 安装：`npm install frorz-lib`
- npm registry：https://registry.npmjs.org/frorz-lib
