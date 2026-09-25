# auto-package-lock

> 标签: npm, package

## 简介

1. 项目 A 安装了依赖软件 B，B 项目内自己依赖了上游库 C。 2. 现 C 出现了 CVE 漏洞，社区发布了新版本修补了漏洞。 3. 但是 B 并未发布新版本引入 C 的无漏洞版本。 4. A 想要避免项目中出现 C 的漏洞，但无法简单通过`npm install C@4.0.7`命令安装指定版本，因为在 package.json 中 A 只与 B 有依赖关系。 5. 因此需要手动修改 A 项目中的 package-lock.json 文件

## 官网

- 官网：https://github.com/Alanscut/auto-package-lock#readme
- 源码仓库：git+https://github.com/Alanscut/auto-package-lock.git
- npm 页面：https://www.npmjs.com/package/auto-package-lock

## 历史版本号

- 当前版本：1.1.0

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.0.5
- 1.1.0

## 获取地址

- npm 安装：`npm install auto-package-lock`
- npm registry：https://registry.npmjs.org/auto-package-lock
