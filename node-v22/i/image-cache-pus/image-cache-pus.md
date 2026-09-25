# image-cache-pus

> 标签: image, image-cahce

## 简介

image-cache 组件是对微信小程序原生 image 组件的封装，通过本地缓存机制优化图片加载性能，能够当第一次请求图片时，组件会将图片下载并存储到本地。后续相同图片的请求，组件会优先检查本地缓存，直接加载已经缓存的图片，避免再次发起网络请求。这不仅减少了服务器压力，还显著提升了图片加载速度，尤其是在网络环境较差或多次使用同一图片的场景中效果尤为明显。避免相同图片的重复下载，提升用户体验和应用性能。

## 官网

- 源码仓库：https://gitee.com/lan-jason/image_cache.git
- npm 页面：https://www.npmjs.com/package/image-cache-pus

## 历史版本号

- 当前版本：1.0.0

- 1.0.0

## 获取地址

- npm 安装：`npm install image-cache-pus`
- npm registry：https://registry.npmjs.org/image-cache-pus
