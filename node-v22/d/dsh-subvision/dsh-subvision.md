# dsh-subvision

> 标签: cordis, deepseek-harness, dsh, image-recognition, plugin, subagent, vision

## 简介

DSH 图片识别插件: 每张图片一个可追问的 vision subagent(标题「识图 | <路径> | <sha256前16>」), 重启后可续问同一子代理; 识别模型默认「自动」= 取目录里第一个可读图的视觉模型(也可显式指定或按图重建); 识图子代理禁用再委派工具, 不会嵌套调用子代理; 图片大小标准化(用户可自定义); Settings 独立「图片代理」页管理每图子代理。

## 官网

- 官网：https://github.com/zglinus-for-agent/dsh-subvision#readme
- 源码仓库：git+https://github.com/zglinus-for-agent/dsh-subvision.git
- npm 页面：https://www.npmjs.com/package/dsh-subvision

## 历史版本号

- 当前版本：0.3.0

- 0.2.0
- 0.2.1
- 0.3.0

## 获取地址

- npm 安装：`npm install dsh-subvision`
- npm registry：https://registry.npmjs.org/dsh-subvision
- Node 要求：>=22.19.0
