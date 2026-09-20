# Awesome Jev Hub Contribution Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make English the canonical Awesome Jev Hub language and add low-friction, category-aware resource submissions with automated repository checks.

**Architecture:** Keep `README.md` as the single source of truth for accepted resources and use `README_CN.md` as the Chinese entry point. Provide an Issue Form for casual contributors and direct README pull requests for experienced contributors. A dependency-free Python validator enforces duplicate-link and entry-format rules in CI.

**Tech Stack:** Markdown, GitHub Issue Forms, GitHub Actions, Python 3 standard library, `unittest`.

**Spec:** `docs/superpowers/specs/2026-09-21-contribution-workflow-design.md`

## Global Constraints

- Work directly on `main` and push after verification, as explicitly requested by the repository owner.
- English is canonical; community resource entries are not duplicated into the Chinese guide.
- Contributors may select existing categories but may not create or rename categories.
- One resource is allowed per submission.
- Do not add runtime dependencies.

---

### Task 1: Canonical English README and Chinese Entry Point

**Files:**
- Modify: `README.md`
- Create: `README_CN.md`
- Delete: `README_EN.md`

**Interfaces:**
- Produces: Stable English category headings consumed by the Issue Form and contribution guide.
- Produces: Top-level `Submit a resource` and `Contribution Guide` links.

- [x] **Step 1: Define the expected documentation structure**

Verify with a shell assertion that the current repository does not yet satisfy the language and contribution-link contract:

```bash
test -f README_CN.md && rg -q 'Submit a resource' README.md
```

Expected: non-zero exit status.

- [x] **Step 2: Make English canonical**

Move the English quick start into `README.md`, move the current Chinese quick start into `README_CN.md`, and remove `README_EN.md`. Add links between the two language entry points.

- [x] **Step 3: Add real category sections and contribution calls to action**

For each community category, add the heading and this empty-state pattern:

```markdown
_No entries yet. [Recommend a resource](https://github.com/rudy2steiner/awesome-jev-hub/issues/new?template=resource.yml)._
```

Keep `Official & Access` maintainer-curated and add a final `Contributing` section linking to `CONTRIBUTING.md`.

- [x] **Step 4: Verify the documentation contract**

Run:

```bash
test -f README_CN.md
test ! -e README_EN.md
rg -q 'Submit a resource' README.md
rg -q '^## Skills & Agents$' README.md
rg -q '^## Contributing$' README.md
```

Expected: all commands exit 0.

### Task 2: Contribution Guide and GitHub Submission Templates

**Files:**
- Create: `CONTRIBUTING.md`
- Create: `.github/ISSUE_TEMPLATE/resource.yml`
- Create: `.github/ISSUE_TEMPLATE/config.yml`
- Create: `.github/PULL_REQUEST_TEMPLATE.md`

**Interfaces:**
- Consumes: Exact category names from `README.md`.
- Produces: A category dropdown for issue submissions and a checklist for direct pull requests.

- [x] **Step 1: Write the contribution guide**

Document eligibility, one-resource-per-submission, objective entry format, evidence requirements, affiliation disclosure, existing-category-only policy, Issue Form instructions, direct PR instructions, and review outcomes.

- [x] **Step 2: Add the resource Issue Form**

Require resource name, URL, category, resource type, practical value, Jev relevance, evidence, language, affiliation, and confirmation checkboxes. Assign `resource-submission` and `needs-review` labels.

- [x] **Step 3: Add repository template configuration**

Disable blank issues and expose contact links to the contribution guide and general discussions/issues page.

- [x] **Step 4: Add the pull request template**

Require one resource per PR, an existing category, the canonical entry format, evidence, affiliation disclosure, and local validator execution.

- [x] **Step 5: Validate template syntax and category consistency**

Run a Python standard-library script that parses all YAML files as text, verifies every required `id`, and confirms every Issue Form category appears as a heading in `README.md`.

Expected: script exits 0 and prints the validated category count.

### Task 3: Test-Driven Resource Validator and CI

**Files:**
- Create: `tests/test_validate_resources.py`
- Create: `scripts/validate_resources.py`
- Create: `.markdownlint.json`
- Create: `.github/workflows/validate.yml`

**Interfaces:**
- Produces: `validate_document(markdown: str) -> list[str]` returning human-readable validation errors.
- Produces: CLI `python3 scripts/validate_resources.py README.md` with exit 0 on success and exit 1 on validation errors.

- [x] **Step 1: Write failing validator tests**

Cover these behaviors using `unittest`:

```python
def test_accepts_unique_well_formed_resource_entries(self): ...
def test_rejects_duplicate_resource_urls(self): ...
def test_rejects_resource_entry_without_description(self): ...
def test_ignores_navigation_and_badge_links(self): ...
```

- [x] **Step 2: Run tests and verify RED**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: import failure because `scripts.validate_resources` does not exist.

- [x] **Step 3: Implement the minimal validator**

Use regular expressions from the standard library to inspect Markdown bullet entries. Treat bullets matching `- [Name](https://...) — Description.` as resources; report likely malformed resource bullets under community category headings and duplicate resource URLs.

- [x] **Step 4: Run tests and verify GREEN**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_resources.py README.md
```

Expected: all tests pass and README validation exits 0.

- [x] **Step 5: Add Markdown and link-check configuration**

Configure Markdown lint to allow the repository's deliberate long lines and inline HTML anchors while retaining structural checks. Limit network-dependent link checking to the public-facing README and contribution guide files.

- [x] **Step 6: Add continuous integration**

Create a GitHub Actions workflow using Python 3.12 that runs the unit tests, resource validator, Markdown lint, and external-link checker on pull requests and pushes to `main`.

- [x] **Step 7: Verify workflow references**

Run:

```bash
rg -q 'python3 -m unittest discover -s tests -v' .github/workflows/validate.yml
rg -q 'python3 scripts/validate_resources.py README.md' .github/workflows/validate.yml
rg -q 'markdownlint-cli2-action@v24' .github/workflows/validate.yml
rg -q 'lychee-action@v2' .github/workflows/validate.yml
```

Expected: all commands exit 0.

### Task 4: Final Repository Verification and Delivery

**Files:**
- Modify: plan checkboxes in `docs/superpowers/plans/2026-09-21-contribution-workflow.md`

**Interfaces:**
- Consumes: All artifacts from Tasks 1–3.
- Produces: Verified commit on `main`, pushed to `origin/main`.

- [x] **Step 1: Run the complete verification suite**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_resources.py README.md
git diff --check
```

Expected: tests pass, validator reports success, and `git diff --check` exits 0.

- [x] **Step 2: Review the final diff and requirements**

Confirm English is canonical, Chinese entry point exists, both submission paths are documented, every community category has a submission call to action, templates use the same category names, and CI invokes the tested validator.

- [ ] **Step 3: Commit and push**

```bash
git add README.md README_CN.md README_EN.md CONTRIBUTING.md .github scripts tests docs/superpowers
git commit -m "feat: add community contribution workflow"
git push origin main
```

- [ ] **Step 4: Confirm the remote branch**

```bash
git status --short --branch
git log -1 --oneline
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Expected: the worktree is clean and the local and remote `main` hashes match.
