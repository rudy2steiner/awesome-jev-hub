# Awesome Jev Hub

> An English-first, developer-focused hub for Jev: trusted resources, runnable examples, agent skills, independent evaluations, and ecosystem updates.

[中文](./README_CN.md) · [Submit a resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml) · [Contribution Guide](./CONTRIBUTING.md)

## Contents

- [Run Jev Now](#run-jev-now)
- [Jev on One Screen](#jev-on-one-screen)
- [Know Before You Build](#know-before-you-build)
- [Recently Added](#recently-added)
- [Official & Access](#official--access)
- [Skills & Agents](#skills--agents)
- [Developer Ecosystem](#developer-ecosystem)
- [Patterns & Cookbook](#patterns--cookbook)
- [Projects by Use Case](#projects-by-use-case)
- [Playgrounds & Reproducible Demos](#playgrounds--reproducible-demos)
- [Benchmarks & Evidence](#benchmarks--evidence)
- [Failures & Limitations](#failures--limitations)
- [Learn](#learn)
- [Open Alternatives](#open-alternatives)
- [Ecosystem Radar](#ecosystem-radar)
- [Contributing](#contributing)

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

## Jev on One Screen

Jev is a model exposed through TypeSafe's System One API for turning input state into typed, structured answers. A request can ask several questions at once and combine Noul, Choice, and Score outputs. Start with [Run Jev Now](#run-jev-now), then use the official documentation as the protocol source of truth.

## Know Before You Build

- Prefer the official API reference over copied request examples because the model and SDKs can change quickly.
- Keep API keys in environment variables or a secret manager; never commit them.
- Record the model name, input, question definitions, and expected output shape in reproducible examples.
- Treat community benchmarks as evidence for a specific setup, not as universal model rankings.

## Recently Added

- **2026-09-21:** Added the English quick start covering the Playground, HTTP API, Python and TypeScript SDKs, and the official Agent Skill.

## Official & Access

This section is maintained from first-party TypeSafe sources.

- [Documentation](https://docs.typesafe.ai) — Product concepts, guides, SDK documentation, and API reference.
- [Playground](https://console.typesafe.ai/playground) — Browser-based environment for trying Jev inputs and structured questions.
- [Console](https://console.typesafe.ai/keys) — Account and API-key management.
- [Official Agent Skill](https://github.com/typesafe-ai/skills) — TypeSafe's skill package for supported coding agents.

## Skills & Agents

_No entries yet. [Recommend a Skills & Agents resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Developer Ecosystem

_No entries yet. [Recommend a Developer Ecosystem resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Patterns & Cookbook

_No entries yet. [Recommend a Patterns & Cookbook resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Projects by Use Case

_No entries yet. [Recommend a Projects by Use Case resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Playgrounds & Reproducible Demos

_No entries yet. [Recommend a Playgrounds & Reproducible Demos resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Benchmarks & Evidence

_No entries yet. [Recommend a Benchmarks & Evidence resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Failures & Limitations

_No entries yet. [Recommend a Failures & Limitations resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Learn

_No entries yet. [Recommend a learning resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Open Alternatives

_No entries yet. [Recommend an Open Alternatives resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Ecosystem Radar

_No entries yet. [Recommend an Ecosystem Radar resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._

## Contributing

Contributions are welcome. Use the [resource submission form](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml) if you want the maintainers to place an item for you, or follow the [Contribution Guide](./CONTRIBUTING.md) to add one resource directly to an existing category.
