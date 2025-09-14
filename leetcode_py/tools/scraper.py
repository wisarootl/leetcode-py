"""LeetCode GraphQL API scraper to fetch problem information."""

from typing import Any

import requests

from .parser import HTMLParser

GRAPHQL_URL = "https://leetcode.com/graphql"
ALGORITHMS_API_URL = "https://leetcode.com/api/problems/algorithms/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

COMMON_SLUGS = {
    1: "two-sum",
    2: "add-two-numbers",
    3: "longest-substring-without-repeating-characters",
    15: "3sum",
    20: "valid-parentheses",
    21: "merge-two-sorted-lists",
    53: "maximum-subarray",
    121: "best-time-to-buy-and-sell-stock",
    125: "valid-palindrome",
    226: "invert-binary-tree",
}


class LeetCodeScraper:
    def __init__(self):
        self.base_url = GRAPHQL_URL
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        }

    def get_problem_by_slug(self, problem_slug: str) -> dict[str, Any] | None:
        query = """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                content
                difficulty
                topicTags {
                    name
                }
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                exampleTestcases
            }
        }
        """

        variables = {"titleSlug": problem_slug}
        response = requests.post(
            self.base_url, json={"query": query, "variables": variables}, headers=self.headers
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("question")
        return None

    def get_problem_by_number(self, problem_number: int) -> dict[str, Any] | None:
        # First try to get slug from algorithms API
        slug = self._get_slug_by_number(problem_number)
        if slug:
            return self.get_problem_by_slug(slug)

        return self._try_common_slugs(problem_number)

    def _get_slug_by_number(self, problem_number: int) -> str | None:
        try:
            response = requests.get(ALGORITHMS_API_URL, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                for problem in data.get("stat_status_pairs", []):
                    if problem["stat"]["frontend_question_id"] == problem_number:
                        return problem["stat"]["question__title_slug"]
        except Exception:
            pass
        return None

    def _try_common_slugs(self, problem_number: int) -> dict[str, Any] | None:
        if problem_number in COMMON_SLUGS:
            return self.get_problem_by_slug(COMMON_SLUGS[problem_number])
        return None

    def get_python_code(self, problem_info: dict[str, Any]) -> str | None:
        if not problem_info or "codeSnippets" not in problem_info:
            return None

        for snippet in problem_info["codeSnippets"]:
            if snippet.get("langSlug") == "python3":
                return snippet.get("code")
        return None

    def format_problem_info(self, problem_info: dict[str, Any]) -> dict[str, Any]:
        if not problem_info:
            return {}

        topics = [tag["name"] for tag in problem_info.get("topicTags", [])]
        python_code = self.get_python_code(problem_info)

        # Parse content for description, examples, and constraints
        content = problem_info.get("content", "")
        parsed_content = HTMLParser.parse_content(content)

        # Parse test cases
        test_cases = HTMLParser.parse_test_cases(problem_info.get("exampleTestcases", ""))

        return {
            "number": problem_info.get("questionFrontendId"),
            "title": problem_info.get("title"),
            "slug": problem_info.get("titleSlug"),
            "difficulty": problem_info.get("difficulty"),
            "topics": topics,
            "description": parsed_content["description"],
            "examples": parsed_content["examples"],
            "constraints": parsed_content["constraints"],
            "python_code": python_code,
            "test_cases": test_cases,
            "raw_content": content,
        }
