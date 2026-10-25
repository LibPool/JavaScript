# dsh-patent-claim-annotation

> 标签: annotation, cordis, deepseek-harness, dsh, dsh-plugin, patent, pdf, pdf-lib, 专利, 具体实施方式, 权利要求

## 简介

DSH 插件：输入专利 PDF，定位权利要求书与说明书【具体实施方式】，在实施方式段落左侧以红色大括号 + 红字标签标出各权利要求对应之处（标签规范：首现裸号「权1」、复现括注「权1(特征)」、多权逗号列表「权1(机架),2,3」，groups 结构化自动合成）；连续同类段落合并为一个括号，跨页在页内断开并标注「（续）」（续标单独占行、与主体同字号）；无文字层时用插件内 Tesseract / Windows.Media.Ocr 识别，或用外部权威文本直接合成透明文字层；附计划留痕（<输出>.plan.j

## 官网

- 官网：https://gitee.com/hc905/dsh-patent-claim-annotation
- 源码仓库：git+https://gitee.com/hc905/dsh-patent-claim-annotation.git
- npm 页面：https://www.npmjs.com/package/dsh-patent-claim-annotation

## 历史版本号

- 当前版本：1.2.0

- 0.0.0-stage
- 1.0.0
- 1.0.1
- 1.1.0
- 1.2.0

## 获取地址

- npm 安装：`npm install dsh-patent-claim-annotation`
- npm registry：https://registry.npmjs.org/dsh-patent-claim-annotation
