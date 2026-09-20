#!/usr/bin/env python3
"""Validate community resource entries in the canonical README."""

from __future__ import annotations

import re
import sys
from pathlib import Path


COMMUNITY_CATEGORIES = {
    "Skills & Agents",
    "Developer Ecosystem",
    "Patterns & Cookbook",
    "Projects by Use Case",
    "Playgrounds & Reproducible Demos",
    "Benchmarks & Evidence",
    "Failures & Limitations",
    "Learn",
    "Open Alternatives",
    "Ecosystem Radar",
}

HEADING_PATTERN = re.compile(r"^## ([^#].*)$")
LINK_BULLET_PATTERN = re.compile(r"^- \[[^]]+\]\([^)]+\)")
RESOURCE_PATTERN = re.compile(
    r"^- \[(?P<name>[^]]+)\]\((?P<url>https://[^)\s]+)\) — "
    r"(?P<description>[A-Z0-9][^\n]*\.)$"
)


def validate_document(markdown: str) -> list[str]:
    """Return validation errors for community resource entries."""
    errors: list[str] = []
    current_category: str | None = None
    seen_urls: dict[str, int] = {}

    for line_number, line in enumerate(markdown.splitlines(), start=1):
        heading = HEADING_PATTERN.match(line)
        if heading:
            title = heading.group(1)
            current_category = title if title in COMMUNITY_CATEGORIES else None
            continue

        if current_category is None or not LINK_BULLET_PATTERN.match(line):
            continue

        resource = RESOURCE_PATTERN.fullmatch(line)
        if resource is None:
            errors.append(
                f"line {line_number}: expected "
                "'- [Name](https://...) — Description.'"
            )
            continue

        url = resource.group("url").rstrip("/")
        if url in seen_urls:
            errors.append(
                f"line {line_number}: duplicate resource URL {url} "
                f"(first used on line {seen_urls[url]})"
            )
        else:
            seen_urls[url] = line_number

    return errors


def main(arguments: list[str] | None = None) -> int:
    """Validate one Markdown file and return a process exit code."""
    args = sys.argv[1:] if arguments is None else arguments
    if len(args) != 1:
        print("Usage: python3 scripts/validate_resources.py README.md")
        return 2

    path = Path(args[0])
    errors = validate_document(path.read_text(encoding="utf-8"))
    if errors:
        print(f"Resource validation failed for {path}:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Resource validation passed for {path}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
