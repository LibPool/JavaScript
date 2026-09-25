# lite-ts-thread

> 标签: thread, ts

## 简介

```typescript const mutex: MutexBase; // 获取 key 等待锁, (最多尝试获取30次，每次间隔在10~20毫秒)，获取不到则抛出异常 const unlock = await mutex.lock({     key: 'key',     tryCount: 30,     sleepRange: [10, 20] }); await unlock(); // 释放锁

## 官网

- npm 页面：https://www.npmjs.com/package/lite-ts-thread

## 历史版本号

- 当前版本：11.4.0

- 1.0.0
- 1.1.0
- 1.2.0
- 11.2.0
- 11.3.0
- 11.4.0
- 3.2.0

## 获取地址

- npm 安装：`npm install lite-ts-thread`
- npm registry：https://registry.npmjs.org/lite-ts-thread
