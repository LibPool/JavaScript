# dsh-local-loop-fuse

> 标签: deepseek-harness, dsh, dsh-plugin, ftllm, guard, loop

## 简介

DSH 循环护栏：① assistant-stream 字符重复检测（可 abort）；①b 低多样性高重复（末窗 + 滑窗两支，抓「带噪声的交替空转」与「正常推理里夹一段空转」——① 线的精确匹配结构上抓不到它们）；①c ① 线命中时注入「停止」类词 + 预注册观测（注入是温和动作，先于掐断）；② 行动层「无进展」停滞检测；②b 同参工具调用连击（按**动作参数**判定，忽略 description 之类自注）；③ 反复卡住达阈值 ⇒ agent.cancel() 真切断；⑤ 零正文 turn（只有思考

## 官网

- 官网：https://github.com/zimuhuan-code/dsh-local-loop-fuse#readme
- 源码仓库：git+https://github.com/zimuhuan-code/dsh-local-loop-fuse.git
- npm 页面：https://www.npmjs.com/package/dsh-local-loop-fuse

## 历史版本号

- 当前版本：0.8.3

- 0.7.0
- 0.7.1
- 0.7.2
- 0.7.3
- 0.7.4
- 0.7.5
- 0.7.6
- 0.8.1
- 0.8.2
- 0.8.3

## 获取地址

- npm 安装：`npm install dsh-local-loop-fuse`
- npm registry：https://registry.npmjs.org/dsh-local-loop-fuse
- Node 要求：>=20
