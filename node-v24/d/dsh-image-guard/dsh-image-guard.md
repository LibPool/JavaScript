# dsh-image-guard

> 标签: context, deepseek, dsh, dsh-plugin, guard, harness, image, images, limit-mm-per-prompt, multimodal, vision, vllm

## 简介

DeepSeek Harness plugin: trims the oldest images from outgoing chat requests and, when the provider rejects the image count with HTTP 400, parses the limit from the error and retries with fewer images. · DSH 插件：裁剪即将发出请求中的历史图片，并在上游因图片数量返回 400 时解析该上限并按更少的图片

## 官网

- 官网：https://github.com/mafeis/dsh-image-guard
- 源码仓库：git+https://github.com/mafeis/dsh-image-guard.git
- npm 页面：https://www.npmjs.com/package/dsh-image-guard

## 历史版本号

- 当前版本：0.8.17

- 0.8.17

## 获取地址

- npm 安装：`npm install dsh-image-guard`
- npm registry：https://registry.npmjs.org/dsh-image-guard
- Node 要求：>=20
