"""HTML parsing utilities for LeetCode problem content."""

import re
from typing import Any


class HTMLParser:
    """Parser for LeetCode HTML content."""

    @staticmethod
    def clean_html(text: str) -> str:
        """Remove HTML tags for clean text."""
        return re.sub(r"<[^>]+>", "", text).strip()

    @staticmethod
    def parse_content(html_content: str) -> dict[str, Any]:
        """Parse HTML content to extract description, examples, and constraints."""
        # Extract description (everything before first example)
        desc_match = re.search(
            r'<p>(.*)(?=<p><strong class="example">|<p><strong>Constraints:|$)', html_content, re.DOTALL
        )
        description = HTMLParser.clean_html(desc_match.group(1)) if desc_match else ""

        # Extract examples
        examples = []
        example_pattern = (
            r'<p><strong class="example">Example (\d+):</strong></p>\s*<pre>\s*(.*)\s*</pre>'
        )
        for match in re.finditer(example_pattern, html_content, re.DOTALL):
            example_num = match.group(1)
            example_text = HTMLParser.clean_html(match.group(2))
            examples.append({"number": int(example_num), "text": example_text})

        # Extract constraints
        constraints_match = re.search(
            r"<p><strong>Constraints:</strong></p>\s*<ul>(.*?)</ul>", html_content, re.DOTALL
        )
        constraints = []
        if constraints_match:
            constraint_items = re.findall(r"<li>(.*?)</li>", constraints_match.group(1))
            constraints = [HTMLParser.clean_html(item) for item in constraint_items]

        return {"description": description, "examples": examples, "constraints": constraints}

    @staticmethod
    def parse_test_cases(test_cases_str: str) -> list[list[str]]:
        """Parse test cases from the exampleTestcases string."""
        if not test_cases_str:
            return []

        # Split by newlines and group into test cases
        lines = [line.strip() for line in test_cases_str.split("\n") if line.strip()]

        # Group lines into test cases
        test_cases = []
        current_case = []

        for line in lines:
            if line.startswith("[") or line.startswith('"') or line.isdigit() or line.startswith("-"):
                current_case.append(line)
            else:
                if current_case:
                    test_cases.append(current_case)
                    current_case = [line]

        if current_case:
            test_cases.append(current_case)

        return test_cases
