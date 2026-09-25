# postcss-plugins-px2rem

> 标签: 3x, px2rem, rem

## 简介

* 应用中,对字体大小不使用`rem`, rem的基准值与屏幕宽度成正比, 这就造成相同分辨率的屏幕,越宽字越大,越窄字越小, 在开发过程中,我们创造了 `dpx` (dpr px) 这个单位, 按照dpr来放大 1*px, 2*px, 3*px 大小的字体,再按照屏幕dpr缩小, 这样就达到了字体 不缩放, 各种屏幕的字体看起来都差不多,也与屏幕宽度无关。 * 边框一般不使用`rem` , 在移动设备上最常见的就是`1px`的边框, 由上一条规则我们知道`rem`无法精确到`1px`, 它只是一个与屏幕

## 官网

- 官网：https://github.com/ggpp224/postcss-plugin-px2rem#readme
- 源码仓库：git+https://github.com/ggpp224/postcss-plugin-px2rem.git
- npm 页面：https://www.npmjs.com/package/postcss-plugins-px2rem

## 历史版本号

- 当前版本：0.0.5

- 0.0.1
- 0.0.3
- 0.0.4
- 0.0.5

## 获取地址

- npm 安装：`npm install postcss-plugins-px2rem`
- npm registry：https://registry.npmjs.org/postcss-plugins-px2rem
- Node 要求：>= 0.10.0
