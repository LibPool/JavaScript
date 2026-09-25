# eslint-plugin-cypress-silent-pass

> 标签: assertions, cypress, eslint, eslint-plugin, eslintplugin, silent-pass, testing

## 简介

ESLint rule that flags Cypress chai assertions that always pass — cy.get() yields a chainable object that always exists, so expect(cy.get('.x')).to.exist / .to.be.ok / .not.to.be.null can never fail. Auto-fixable.

## 官网

- 官网：https://github.com/voidmatcha/eslint-plugin-cypress-silent-pass#readme
- 源码仓库：git+https://github.com/voidmatcha/eslint-plugin-cypress-silent-pass.git
- npm 页面：https://www.npmjs.com/package/eslint-plugin-cypress-silent-pass

## 历史版本号

- 当前版本：0.2.2

- 0.1.0
- 0.1.1
- 0.1.2
- 0.2.0
- 0.2.1
- 0.2.2

## 获取地址

- npm 安装：`npm install eslint-plugin-cypress-silent-pass`
- npm registry：https://registry.npmjs.org/eslint-plugin-cypress-silent-pass
- Node 要求：>=18
