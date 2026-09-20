import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_resources import validate_document


class ValidateDocumentTests(unittest.TestCase):
    def test_accepts_unique_well_formed_resource_entries(self):
        markdown = """\
## Skills & Agents

- [Jev Skill](https://example.com/skill) — Adds a tested Jev workflow.

## Learn

- [Jev Guide](https://example.com/guide) — Explains structured questions with examples.
"""

        self.assertEqual(validate_document(markdown), [])

    def test_rejects_duplicate_resource_urls(self):
        markdown = """\
## Skills & Agents

- [Jev Skill](https://example.com/shared) — Adds a tested Jev workflow.

## Learn

- [Jev Guide](https://example.com/shared) — Explains the same resource.
"""

        errors = validate_document(markdown)

        self.assertEqual(len(errors), 1)
        self.assertIn("duplicate resource URL", errors[0])
        self.assertIn("https://example.com/shared", errors[0])

    def test_rejects_resource_entry_without_description(self):
        markdown = """\
## Skills & Agents

- [Jev Skill](https://example.com/skill)
"""

        errors = validate_document(markdown)

        self.assertEqual(len(errors), 1)
        self.assertIn("expected '- [Name](https://...) — Description.'", errors[0])

    def test_ignores_navigation_and_links_outside_community_categories(self):
        markdown = """\
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Contents

- [Skills & Agents](#skills--agents)

## Official & Access

- [Documentation](https://docs.typesafe.ai) — Official documentation.
"""

        self.assertEqual(validate_document(markdown), [])


class ValidatorCliTests(unittest.TestCase):
    def test_cli_returns_nonzero_for_an_invalid_document(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory, "README.md")
            readme.write_text(
                "## Learn\n\n- [Broken](https://example.com/broken)\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, "scripts/validate_resources.py", str(readme)],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Resource validation failed", result.stdout)


if __name__ == "__main__":
    unittest.main()
