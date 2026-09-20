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
