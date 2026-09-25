# egg-api-auth

> 标签: egg, egg-plugin, eggPlugin

## 简介

签名规则如下:   1.我们会颁发给调用者一个clientID和accessKey,也就是调用者ID和秘钥.   2.每个接口除了业务参数外需要传递公共参数cilentID和timestamp以及nonce,     timestamp为当前时间戳,格式为整数:new Date().getTime(),nonce为随机数,随机数是为了防止重放攻击   3.请求接口时候,将所有请求参数(包括公共参数)集合按照参数名ASCII码从小到大排序,     然后使用URL键值对的格式(即key1=value1&ke

## 官网

- 官网：https://github.com/holyselina/egg-api-auth#readme
- 源码仓库：git+https://github.com/holyselina/egg-api-auth.git
- npm 页面：https://www.npmjs.com/package/egg-api-auth

## 历史版本号

- 当前版本：2.3.0

- 1.0.0
- 1.0.1
- 1.0.2
- 1.0.3
- 1.1.3
- 2.0.0
- 2.1.0
- 2.2.0
- 2.3.0

## 获取地址

- npm 安装：`npm install egg-api-auth`
- npm registry：https://registry.npmjs.org/egg-api-auth
- Node 要求：>=8.0.0
