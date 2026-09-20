# Awesome Jev Hub 首版 README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 创建中英双语 README 目录，并完成首个 `Run Jev Now / 立即体验` 栏目，让读者可以从官方 Playground、API、SDK 或 Agent Skill 立即开始。

**Architecture:** `README.md` 是中文主入口，`README_EN.md` 是结构完全对应的英文入口。当前批次只让已完成的 `Run Jev Now` 成为可点击目录项，未完成栏目保留为纯文本目录，避免制造失效锚点；动态事实都标注核查日期并链接一手来源。

**Tech Stack:** Markdown、GitHub Markdown anchors、shell (`rg`、`curl`、`git`)

**Spec:** `docs/superpowers/specs/2026-09-20-awesome-jev-hub-readme-design.md`

## Global Constraints

- 中文与英文内容保持相同结构，分别维护在 `README.md` 和 `README_EN.md`。
- 官方声明、作者自测和第三方复现必须明确区分。
- 动态信息标注核查日期；价格、限额、模型版本等不写成永久事实。
- 一个资源只进入一个主分类，其他属性使用标签表达。
- 每个项目至少说明：解决的问题、Jev 承担的决策、运行入口、验证状态和最后核查日期。
- 当前批次不建设独立网站、搜索、排行榜或自动采集系统。
- 不复述未经核查的性能、准确率或“零幻觉”营销结论。
- 不在仓库、示例或命令中写入真实 API Key。
- 当前批次事实核查日期统一为 `2026-09-21`。

## File Structure

- Modify: `README.md` — 中文主入口、完整规划目录、中文 `Run Jev Now`。
- Create: `README_EN.md` — 英文镜像入口、相同目录、英文 `Run Jev Now`。
- Reference: `docs/superpowers/specs/2026-09-20-awesome-jev-hub-readme-design.md` — 已批准的范围与验收标准，不修改。

---

### Task 1: 中文 README 目录与立即体验

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: 设计稿中的 16 个目录项；TypeSafe 官方 Quick Start、JavaScript SDK 和 Skills 安装方式。
- Produces: 中文主入口和稳定锚点 `run-jev-now`，供英文 README 与后续栏目沿用。

- [ ] **Step 1: 检查现有 README，确认只包含初始化标题**

Run:

```bash
sed -n '1,80p' README.md
git status --short README.md
```

Expected: 文件包含 `# awesome-jev-hub`；Git 状态显示该文件已加入索引。不要清除用户已有的索引状态。

- [ ] **Step 2: 用以下完整结构替换中文 README**

```markdown
# Awesome Jev Hub

> 中文优先、双语维护的 Jev 开发者实践中心：可信资源、可运行示例、Agent Skills、独立评测与生态动态。

[English](./README_EN.md)

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
```

- [ ] **Step 3: 验证中文 README 的目录与首段结构**

Run:

```bash
rg -n '^#|^<a id=|^- \[|^- [A-Z]' README.md
```

Expected:

- 一个 H1 标题。
- 16 个目录项，只有已完成的 `Run Jev Now` 使用 Markdown 链接。
- 一个 `<a id="run-jev-now"></a>`。
- `Run Jev Now` 下有四个 H3 子节。

- [ ] **Step 4: 检查 Markdown 空白和补丁质量**

Run:

```bash
git diff --check -- README.md
git diff -- README.md
```

Expected: `git diff --check` 无输出；diff 只包含预期的中文 README 内容。

- [ ] **Step 5: 提交中文 README**

```bash
git add README.md
git commit -m "docs: add Chinese Jev quick start"
```

---

### Task 2: 英文 README 镜像

**Files:**
- Create: `README_EN.md`

**Interfaces:**
- Consumes: Task 1 产生的目录顺序、`run-jev-now` 锚点和已核查命令。
- Produces: 自然英文表达的镜像 README；后续两个文件可按相同目录逐节扩展。

- [ ] **Step 1: 创建英文 README，使用以下完整内容**

```markdown
# Awesome Jev Hub

> A bilingual, developer-first hub for Jev: trusted resources, runnable examples, agent skills, independent evaluations, and ecosystem updates.

[中文](./README.md)

## Table of Contents

- [Run Jev Now](#run-jev-now)
- Jev on One Screen
- Know Before You Build
- Recently Added
- Official & Access
- Skills & Agents
- Developer Ecosystem
- Patterns & Cookbook
- Projects by Use Case
- Playgrounds & Reproducible Demos
- Benchmarks & Evidence
- Failures & Limitations
- Learn
- Open Alternatives
- Ecosystem Radar
- Contributing

<a id="run-jev-now"></a>
## Run Jev Now

Want to run Jev before studying the details? These four paths come from TypeSafe's official resources. Pick the one closest to your current setup.

> **Source status:** Official · **Last checked:** 2026-09-21

| Path | Best for | Prerequisites | Time |
| --- | --- | --- | --- |
| [Official Playground](https://console.typesafe.ai/playground) | Seeing the input and structured output first | TypeSafe account | 2–3 minutes |
| cURL / HTTP API | Inspecting the request protocol directly | TypeSafe API key and cURL | 5 minutes |
| Python or TypeScript SDK | Adding Jev to an application | API key; Python 3.10+ or Node.js 20+ | 10 minutes |
| Official Agent Skill | Claude Code, Codex, Cursor, and other coding-agent users | Claude Code, or Node.js with `npx` | 2 minutes |

### 1. Try the Playground

Open the [TypeSafe Playground](https://console.typesafe.ai/playground), sign in, paste some text as the `state`, and add a Noul question:

```json
{
  "urgency": {
    "type": "noul",
    "instructions": "Does this message express urgency?"
  }
}
```

One request can mix Noul, Choice, and Score questions. See the [official Quick Start](https://docs.typesafe.ai/introduction/quickstart) for the complete walkthrough.

### 2. Make Your First API Call

Create an API key in the [TypeSafe Console](https://console.typesafe.ai/keys), then keep it in an environment variable:

```bash
export TYPESAFE_API_KEY="your-key"
```

Send a minimal request:

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

The response contains a structured answer named `urgency` instead of generated prose. Treat the [official API Reference](https://docs.typesafe.ai/api) as the source of truth for the protocol.

### 3. Use an SDK

Python:

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

JavaScript / TypeScript:

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

See the official [Python SDK](https://docs.typesafe.ai/sdk/python) and [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript) documentation.

### 4. Install the Official Agent Skill

Claude Code:

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

Other agents that support skills:

```bash
npx skills add typesafe-ai/skills --skill typesafe-ai
```

The installer prompts you to choose a target agent. Installation is project-local by default; add `-g` for a global installation. See [typesafe-ai/skills](https://github.com/typesafe-ai/skills) for the source and usage guide.
```

- [ ] **Step 2: 验证中英文目录顺序和锚点一致**

Run:

```bash
rg -n '^#|^<a id=|^- \[|^- [A-Z]' README_EN.md
diff -u \
  <(rg -o '<a id="[^"]+"' README.md) \
  <(rg -o '<a id="[^"]+"' README_EN.md)
```

Expected: 英文文件有 16 个同序目录项和四个 H3 子节；`diff` 无输出。

- [ ] **Step 3: 检查英文 Markdown 质量**

Run:

```bash
git diff --check -- README_EN.md
git diff -- README_EN.md
```

Expected: `git diff --check` 无输出；英文表达自然，不出现中文正文，语言切换链接指向 `README.md`。

- [ ] **Step 4: 提交英文 README**

```bash
git add README_EN.md
git commit -m "docs: add English Jev quick start"
```

---

### Task 3: 一手来源与最终验收

**Files:**
- Verify: `README.md`
- Verify: `README_EN.md`

**Interfaces:**
- Consumes: 两个 README 中的相同 URL、命令、锚点和核查日期。
- Produces: 无失效官方链接、无 Markdown 空白错误、工作区状态清晰的首版交付。

- [ ] **Step 1: 检查所有一手来源链接**

Run:

```bash
for url in \
  https://console.typesafe.ai/playground \
  https://console.typesafe.ai/keys \
  https://docs.typesafe.ai/introduction/quickstart \
  https://docs.typesafe.ai/api \
  https://docs.typesafe.ai/sdk/python \
  https://docs.typesafe.ai/sdk/javascript \
  https://github.com/typesafe-ai/skills; do
  curl -L --fail --silent --show-error -o /dev/null "$url"
done
```

Expected: 命令退出码为 0；所有 URL 可访问或正常跳转到登录页。

- [ ] **Step 2: 检查目录、版本事实和敏感信息**

Run:

```bash
rg -n '2026-09-21|Python 3\.10\+|Node\.js 20\+' README.md README_EN.md
rg -n 'sk-[A-Za-z0-9]{20,}|TYPESAFE_API_KEY="[A-Za-z0-9_-]{20,}"' README.md README_EN.md || true
```

Expected:

- 两个文件都出现相同核查日期和运行时要求。
- 第二条命令无输出；示例只出现环境变量名和虚拟值 `your-key`，没有真实凭据。

- [ ] **Step 3: 运行最终 Git 检查**

Run:

```bash
git diff --check HEAD
git status --short
git log --oneline -3
```

Expected:

- `git diff --check HEAD` 无输出。
- README 相关改动已提交。
- 最近提交包含中文和英文 Quick Start 两个提交；设计稿提交仍在历史中。

- [ ] **Step 4: 若验收修复产生改动，提交修复**

仅当 Step 1–3 发现并修复问题时运行：

```bash
git add README.md README_EN.md
git commit -m "docs: fix Jev quick start verification issues"
```

Expected: 无修复时跳过；有修复时提交仅包含验收所需调整。
