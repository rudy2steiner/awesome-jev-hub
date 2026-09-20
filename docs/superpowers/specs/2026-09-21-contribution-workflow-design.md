# Awesome Jev Hub Contribution Workflow Design

## Goal

Make English the canonical repository language and let both GitHub newcomers and experienced contributors recommend one Jev resource under an existing category without changing the taxonomy.

## Content Model

- `README.md` is the canonical English list and contains every accepted entry.
- `README_CN.md` is the Chinese introduction and quick start; it points contributors to the canonical English list instead of duplicating community-maintained entries.
- Categories remain maintainer-owned. Contributors select an existing category.
- Each submission contains exactly one resource and uses an objective one-line description.
- Official resources remain maintainer-curated; community submissions target the other listed categories.

## Submission Paths

1. A prominent `Submit a resource` link opens a GitHub Issue Form with a category dropdown and required evidence fields.
2. Experienced contributors may edit the matching section in `README.md` and open a pull request using the repository template.
3. Pull requests that change list entries are checked for Markdown consistency and duplicate resource URLs.

## Quality Rules

- The resource must be directly relevant to Jev.
- Links must be publicly accessible and not already listed.
- Submissions must explain the practical value and provide evidence such as runnable code, a tested workflow, official documentation, or an independent evaluation.
- Authors and affiliated submitters must disclose their relationship to the resource.
- Promotional copy and multi-resource submissions are rejected.

## Automation

- A dependency-free Python validator checks duplicate Markdown URLs and validates the canonical entry format for newly added list items.
- Unit tests exercise accepted entries, duplicates, malformed entries, and non-resource Markdown links.
- GitHub Actions run the tests, resource validator, Markdown lint, and external-link health check for pull requests and pushes to `main`.

## Growth Path

Keep one human-readable canonical README while the list is small. Migrate to one structured data file per resource and generate the README only after the repository reaches roughly 100 entries or receives more than 10 submissions per month.
