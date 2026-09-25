# hejiahaolib

> 标签: JavaScript

## 简介

$$dp[i][j] = \begin{cases} 0 & j = 0 \\ \min\{dp[i][k] + dp[(i+k+1)\%n][j-k-1] + sum(i,j)\} & 0\leq k < j \end{cases}$$

## 官网

- npm 页面：https://www.npmjs.com/package/hejiahaolib

## 历史版本号

- 当前版本：1.0.2

- 1.0.0
- 1.0.1
- 1.0.2

## 获取地址

- npm 安装：`npm install hejiahaolib`
- npm registry：https://registry.npmjs.org/hejiahaolib
