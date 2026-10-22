# @fulate/ui

> 标签: JavaScript

## 简介

`Bitmap`唯一拥有主线程当前frame，并向位图producer提供`renderPixelRatio = Viewport scale × DPR`。 producer保持authored-local布局；需要超采样时，在自己的backend中基于该倍率增加质量倍率和资源预算。 `paintBitmap()`仍把最终位图绘制到图元authored宽高，再由Layer应用Viewport与DPR。

## 官网

- npm 页面：https://www.npmjs.com/package/@fulate/ui

## 历史版本号

- 当前版本：1.0.19

- 1.0.12
- 1.0.13
- 1.0.14
- 1.0.15
- 1.0.19
- 1.0.2
- 1.0.3
- 1.0.5
- 1.0.6
- 1.0.7
- 1.0.8
- 1.0.9

## 获取地址

- npm 安装：`npm install @fulate/ui`
- npm registry：https://registry.npmjs.org/@fulate/ui
