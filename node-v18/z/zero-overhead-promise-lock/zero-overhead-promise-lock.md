# zero-overhead-promise-lock

> 标签: ES2020, Node.js, access-executing-promise, access-ongoing-task, advanced-usage-patterns, async-lock, async-task-lock, avoid-redundant-executions, backpressure, backpressure-indicator, check-and-abort, clean-teardown, critical-section, disposable, event-loop-iterations, event-loop-lock, graceful-shutdown, graceful-teardown, graceful-termination, is-available, lock, mutex, mutually-exclusive, nodejs, promise-lock, race-condition, rate-limiting, smart-reuse, smooth-teardown, throttle, ts, typescript

## 简介

An efficient Promise lock for Node.js projects, ensuring mutually exclusive execution of asynchronous tasks. Key features include a backpressure indicator, access to the currently executing task promise for smart reuse (useful when launching a duplicate t

## 官网

- 官网：https://github.com/ori88c/zero-overhead-promise-lock#readme
- 源码仓库：git+https://github.com/ori88c/zero-overhead-promise-lock.git
- npm 页面：https://www.npmjs.com/package/zero-overhead-promise-lock

## 历史版本号

- 当前版本：1.2.1

- 1.0.0
- 1.1.0
- 1.1.1
- 1.1.2
- 1.1.3
- 1.1.4
- 1.2.0
- 1.2.1

## 获取地址

- npm 安装：`npm install zero-overhead-promise-lock`
- npm registry：https://registry.npmjs.org/zero-overhead-promise-lock
- Node 要求：>=14.5.0
