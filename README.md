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

- **2026-09-21:** Seeded all ten community categories with 30 curated resources covering skills, integrations, patterns, projects, reproducible evidence, limitations, learning material, and open alternatives.
- **2026-09-21:** Added the English quick start covering the Playground, HTTP API, Python and TypeScript SDKs, and the official Agent Skill.

## Official & Access

This section is maintained from first-party TypeSafe sources.

- [Documentation](https://docs.typesafe.ai) — Product concepts, guides, SDK documentation, and API reference.
- [Playground](https://console.typesafe.ai/playground) — Browser-based environment for trying Jev inputs and structured questions.
- [Console](https://console.typesafe.ai/keys) — Account and API-key management.
- [Official Agent Skill](https://github.com/typesafe-ai/skills) — TypeSafe's skill package for supported coding agents.

## Skills & Agents

- [Official TypeSafe Skill](https://github.com/typesafe-ai/skills/tree/main/skills/typesafe-ai) — Teaches coding agents how to select Jev primitives, design typed questions, call the SDKs, and interpret responses.
- [Jevify](https://github.com/altryne/jevify) — Audits a codebase for useful Jev decision points and supplies question-design, evaluation, and boundary-testing workflows.
- [pi-jev](https://github.com/y0usaf/pi-jev) — Adds measured Jev gates and output judgments to the Pi coding agent, with shadow mode, confidence thresholds, and documented privacy limits.

## Developer Ecosystem

- [Jev MCP](https://github.com/jkudish/jev-mcp) — Exposes Jev verification, screening, routing, extraction, review, and gating workflows as tested MCP tools.
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) — Provides a tested Ruby interface for Noul, Choice, and Score questions with a native TypeSafe provider.
- [Jevex](https://github.com/kentaro/jevex) — Composes Jev decisions with ordinary Elixir control flow and documents confidence gates, fallbacks, and backend contracts.

## Patterns & Cookbook

- [Confidence-Based Routing](https://docs.typesafe.ai/patterns/confidence-routing) — Shows how to route confident answers automatically and send uncertain cases to a fallback path.
- [Parallel Questions](https://docs.typesafe.ai/cookbooks/parallel_questions) — Demonstrates how to evaluate several independent typed questions against one shared state in a single request.
- [TypeSafe Jev Examples](https://github.com/rajivkuriakose/typesafe-jev-examples) — Provides worked Python examples for ticket triage, reranking, and policy decisions with offline policy tests and explicit caveats.

## Projects by Use Case

- [Foreman](https://github.com/thruwire/foreman) — Supervises coding workers with bounded Jev judgments about completion, test sufficiency, progress, and human escalation.
- [Jev Review](https://github.com/devagrawal09/jev-review) — Runs a staged Jev code-review workflow over diffs or codebases and presents evidence-linked findings in a local dashboard.
- [Jev Search](https://github.com/superagents-lab/jev-search) — Uses Jev to choose search parameters and rerank web results while returning source links instead of generated answers.

## Playgrounds & Reproducible Demos

- [TypeSafe AI Community Playground](https://github.com/TypeSafeAI/typesafe-playground) — Offers editable Jev experiments, A/B comparisons, simulations, and documented mock-versus-live execution paths.
- [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) — Demonstrates Jev-driven voice browser control with unit tests, real-call fixtures, latency measurements, and explicit browser limits.
- [Jev Drone](https://github.com/RomanSlack/jev-drone) — Places Jev in an advisory MuJoCo drone loop alongside deterministic safety controls, runnable ablations, telemetry, and candid caveats.

## Benchmarks & Evidence

- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — Presents TypeSafe's vendor-reported architecture, benchmark methodology, calibration results, latency, and pricing evidence.
- [Jev RAG Benchmark](https://github.com/erendikmenn/jev-rag-benchmark) — Publishes a reproducible 1,044-query Turkish XQuAD study with configurations, raw artifacts, cost data, and negative results.
- [Jev Is Odd](https://github.com/robipop22/Jev-is-odd) — Records a small fixed Jev arithmetic probe with per-request outputs, token usage, latency, cost estimates, and a reproducible benchmark command.

## Failures & Limitations

- [Jev 1.13 Model Jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — Documents first-party failure modes across arithmetic, dates, indirection, irrelevant context, adversarial content, and structured generation.
- [Winnow Jev Contract](https://github.com/ThinkyMiner/Winnow/blob/main/docs/jev-contract.md) — Captures observed live-API behavior, response-shape assumptions, score semantics, and defensive integration rules from a browser extension.
- [Jev Capability Atlas](https://github.com/Zaious/jev-capability-atlas) — Maps strong and weak task shapes with bilingual explanations, real API-call receipts, reusable suites, and source labels.

## Learn

- [Quick Start](https://docs.typesafe.ai/introduction/quickstart) — Walks through the Playground, API keys, first request, typed answers, and basic SDK usage.
- [Decision Primitives](https://docs.typesafe.ai/primitives) — Explains Noul, Choice, and Score outputs and when each primitive fits a decision problem.
- [How to Build with System One](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) — Introduces the design shift from generated text to bounded typed judgments composed in application code.

## Open Alternatives

- [SemIf](https://github.com/TheoLeeCJ/SemIf) — Recreates the typed-decision interface pattern with open models and publishes pinned runners, raw results, known failures, and reproduction guides.
- [Von](https://github.com/wfzyx/von) — Implements a local non-autoregressive decision model with Python and TypeScript clients, hardware-specific runtimes, and benchmark artifacts.
- [Jeff](https://github.com/logan-markewich/jeff) — Provides a self-hosted Jev-compatible server powered by GLiFormer with SDK examples, deployment options, compatibility notes, and benchmarks.

## Ecosystem Radar

- [TypeSafe on X](https://x.com/typesafeai) — Tracks first-party Jev launch and ecosystem updates from the official TypeSafe account; checked 2026-09-21.
- [TypeSafeAI on GitHub](https://github.com/TypeSafeAI) — Surfaces newly published Jev repositories and community experiments under the TypeSafeAI organization; checked 2026-09-21.
- [awesome-jev](https://github.com/yibie/awesome-jev) — Maintains a broad companion index of Jev projects and discussions whose entries are useful as discovery leads rather than quality endorsements.

## Contributing

Contributions are welcome. Use the [resource submission form](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml) if you want the maintainers to place an item for you, or follow the [Contribution Guide](./CONTRIBUTING.md) to add one resource directly to an existing category.
