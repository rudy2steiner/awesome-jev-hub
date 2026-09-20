# Awesome Jev Hub

> Awesome Jev Hub 的中文快速入门。社区资源以英文主列表为准，避免双语副本不同步。

[English canonical list](./README.md) · [参与贡献](./CONTRIBUTING.md)

## 目录

- [Run Jev Now / 立即体验](#run-jev-now)
- Jev on One Screen / 一屏认识 Jev
- Know Before You Build / 开发前必读
- Recently Added / 最近收录
- Official & Access / 官方与接入
- Skills & Agents / Skills 与 Agent
- Developer Ecosystem / 开发生态
- Patterns & Cookbook / 模式与实践
- Projects by Use Case / 按场景浏览项目
- Playgrounds & Reproducible Demos / 演示与复现
- Benchmarks & Evidence / 评测与证据
- Failures & Limitations / 失败实践与局限
- Learn / 学习资料
- Open Alternatives / 开源替代
- Ecosystem Radar / 生态雷达
- Contributing / 参与贡献

<a id="run-jev-now"></a>

## Run Jev Now / 立即体验

想先跑起来，再研究原理？下面四个入口均来自 TypeSafe 官方资料，选择与你当前环境最接近的一种即可。

> **来源状态：** Official · **最近核查：** 2026-09-21

| 路径 | 适合谁 | 前置条件 | 预计耗时 |
| --- | --- | --- | --- |
| [官方 Playground](https://console.typesafe.ai/playground) | 想先观察输入与结构化输出 | TypeSafe 账号 | 2–3 分钟 |
| cURL / HTTP API | 想直接查看请求协议 | TypeSafe API Key、cURL | 5 分钟 |
| Python 或 TypeScript SDK | 准备接入应用的开发者 | API Key；Python 3.10+ 或 Node.js 20+ | 10 分钟 |
| 官方 Agent Skill | 使用 Claude Code、Codex、Cursor 等编码 Agent | Claude Code，或 Node.js 与 `npx` | 2 分钟 |

### 1. 在线体验

打开 [TypeSafe Playground](https://console.typesafe.ai/playground) 并登录，粘贴一段文本作为 `state`，再添加一个 Noul 问题：

```json
{
  "urgency": {
    "type": "noul",
    "instructions": "Does this message express urgency?"
  }
}
```

一次请求可以同时混用 Noul、Choice 和 Score。完整操作见 [官方 Quick Start](https://docs.typesafe.ai/introduction/quickstart)。

### 2. 第一次 API 调用

先在 [TypeSafe Console](https://console.typesafe.ai/keys) 创建 API Key，并只通过环境变量保存：

```bash
export TYPESAFE_API_KEY="your-key"
```

然后发送一个最小请求：

```bash
curl -X POST https://api.typesafe.ai/v1/systemone \
  -H "Authorization: Bearer $TYPESAFE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- <<'EOF'
{
  "state": "The integration keeps failing and I need help ASAP.",
  "model": "jev-latest",
  "questions": {
    "urgency": {
      "type": "noul",
      "instructions": "Does this message express urgency?"
    }
  }
}
EOF
```

请求会返回名为 `urgency` 的结构化答案，而不是生成一段文本。协议细节以 [官方 API Reference](https://docs.typesafe.ai/api) 为准。

### 3. 使用 SDK

Python：

```bash
python -m pip install typesafe-sdk
```

```python
from typesafe_sdk import Noul, TypeSafeClient

client = TypeSafeClient()
response = client.system_one(
    state="The integration keeps failing and I need help ASAP.",
    questions={
        "urgency": Noul(
            instructions="Does this message express urgency?",
        )
    },
)

print(response.answers["urgency"].noul)
```

JavaScript / TypeScript：

```bash
npm install @typesafe-ai/sdk
```

```typescript
import { choice, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient();
const response = await client.systemOne({
  state: { document: "I was charged twice. Please fix this ASAP." },
  questions: {
    category: choice("What is this ticket about?", {
      billing: null,
      technical: null,
      other: null,
    }),
  },
});

console.log(response.answers.category.choice);
```

参见官方 [Python SDK](https://docs.typesafe.ai/sdk/python) 与 [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript)。

### 4. 安装官方 Agent Skill

Claude Code：

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

其他支持 Skills 的 Agent：

```bash
npx skills add typesafe-ai/skills --skill typesafe-ai
```

安装器会提示选择目标 Agent；默认安装到当前项目，添加 `-g` 可全局安装。源码与说明见 [typesafe-ai/skills](https://github.com/typesafe-ai/skills)。
