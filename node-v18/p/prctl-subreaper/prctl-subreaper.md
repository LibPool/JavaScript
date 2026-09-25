# prctl-subreaper

> 标签: PR_SET_CHILD_SUBREAPER, child-process, defunct, init, libuv, linux, node-pid-1, orphan, prctl, process-supervisor, reap, subreaper, tini, tini-alternative, waitpid, zombie

## 简介

Make any Linux Node.js or Bun process a subreaper for its descendants. Calls prctl(PR_SET_CHILD_SUBREAPER, 1) plus runs a polling waitpid reaper for zombies whose ppid is the host process. Closes the libuv #1911 close-before-exit gap and the orphan-repare

## 官网

- 官网：https://github.com/coopergwrenn/prctl-subreaper#readme
- 源码仓库：git+https://github.com/coopergwrenn/prctl-subreaper.git
- npm 页面：https://www.npmjs.com/package/prctl-subreaper

## 历史版本号

- 当前版本：0.1.1

- 0.1.0
- 0.1.1

## 获取地址

- npm 安装：`npm install prctl-subreaper`
- npm registry：https://registry.npmjs.org/prctl-subreaper
- Node 要求：>=14
