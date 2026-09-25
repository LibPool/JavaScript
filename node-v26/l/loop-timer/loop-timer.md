# loop-timer

> 标签: loop, loop-timer, timer

## 简介

模拟 linux Crontab 的 js 定时任务,可以指定时间来执行任务,由于 JS 是单线程,所以如果指定的任务是个大计算量的任务,有可能会导致其他任务被延时执行,如果对时间准确性要求很高的,请慎用. 项目里面同时只会存在一个计时器, 如果有没有可以执行事件的时候,计时器将会被销毁,有新的可执行事件才会再次开启新的计时器.

## 官网

- 官网：https://github.com/xianjixin/loop-timer#readme
- 源码仓库：git+https://github.com/xianjixin/loop-timer.git
- npm 页面：https://www.npmjs.com/package/loop-timer

## 历史版本号

- 当前版本：1.0.6

- 1.0.2
- 1.0.3
- 1.0.5
- 1.0.6

## 获取地址

- npm 安装：`npm install loop-timer`
- npm registry：https://registry.npmjs.org/loop-timer
