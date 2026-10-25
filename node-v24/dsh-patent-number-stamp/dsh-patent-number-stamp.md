# dsh-patent-number-stamp

> 标签: cordis, deepseek-harness, dsh, dsh-plugin, patent, pdf, pdf-lib, 专利, 序号, 标注, 页眉

## 简介

DSH 插件：从 PDF 文件名里提取设定范围内的字符（「涉案专利」/「D数字」/「D数字-数字」/「证据数字」/「证据数字-数字」），以正红大字标到首页页眉空白处（顶部居右，右侧被占自动左让），原地改写并默认留备份；提不到字符报错跳过；文件名出现多个不同数字时不直接加注、报错列候选，待询问用户后用 label 消歧；可选用 label 参数手写指定（与文件名不一致时回显 filenameMismatch 告警）；页眉已有同一字符视为已标注不重复盖；落盘前逐像素自检。

## 官网

- 官网：https://gitee.com/hc905/dsh-patent-number-stamp
- 源码仓库：git+https://gitee.com/hc905/dsh-patent-number-stamp.git
- npm 页面：https://www.npmjs.com/package/dsh-patent-number-stamp

## 历史版本号

- 当前版本：1.3.0

- 0.0.0-stage
- 1.2.0
- 1.3.0

## 获取地址

- npm 安装：`npm install dsh-patent-number-stamp`
- npm registry：https://registry.npmjs.org/dsh-patent-number-stamp
