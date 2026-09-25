# flow-personal-wiki

> 标签: JavaScript

## 简介

로컬에서 도는 Host 에이전트 채팅이다. Next.js 앱 하나가 브라우저 UI와 에이전트 서버를 같이 들고 있고, 한 턴은 `deepagents`/LangGraph 하네스가 돌린다. LLM 키만 있으면 채팅이 열린다(`shouldEnterChat` = `isLlmReady`, `lib/setup-gate.ts`). 위키·MCP·스킬·서브에이전트·웹검색은 그 위에 꽂는 슬롯이고, 하나도 없어도 대화는 된다. Host 프롬프트(`.agents/promp

## 官网

- npm 页面：https://www.npmjs.com/package/flow-personal-wiki

## 历史版本号

- 当前版本：0.1.2

- 0.1.0
- 0.1.1
- 0.1.2

## 获取地址

- npm 安装：`npm install flow-personal-wiki`
- npm registry：https://registry.npmjs.org/flow-personal-wiki
- Node 要求：>=20.9.0
