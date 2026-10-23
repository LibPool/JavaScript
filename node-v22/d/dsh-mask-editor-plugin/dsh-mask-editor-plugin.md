# dsh-mask-editor-plugin

> 标签: annotation, brush, canvas, canvas-editor, client-plugin, deepseek-harness, dsh, dsh-plugin, inpaint, mask, mask-editor, paint, ui

## 简介

DeepSeek Harness 画布插件：canvas_editor —— 调用后在网页端弹出画笔画布（参考 ComfyUI 掩码编辑器），用户亲手涂。画布上有两个互相独立的笔迹层：「掩码」层产出与原图同尺寸的黑白掩码 PNG，「笔迹」层产出把笔迹烧进原图的合成 PNG；画了就是要、没画就是不要，所以两层都画就两个文件都落盘、只画一层就只落那一个、一层都没画就点保存＝放弃这次编辑。工具栏可把一层复制追加到另一层（省得画两遍），画完还能补一句给模型的话。结果自动落盘（路径、尺寸、笔数与覆盖率随工具结果返回

## 官网

- npm 页面：https://www.npmjs.com/package/dsh-mask-editor-plugin

## 历史版本号

- 当前版本：0.1.1

- 0.0.0-stage
- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install dsh-mask-editor-plugin`
- npm registry：https://registry.npmjs.org/dsh-mask-editor-plugin
- Node 要求：>=22
