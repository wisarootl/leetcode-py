# Contributing to LeetCode Practice Repository

Thank you for your interest in contributing! This repository welcomes contributions from the community.

## Ways to Contribute

### 1. Add New Problems

Use an LLM assistant (Cursor, GitHub Copilot Chat, Amazon Q) with the rule files:

- Include `.amazonq/rules/problem-creation.md` in your LLM context
- Ask: "Create LeetCode problem [number] ([name])"

### 2. Enhance Test Cases

- Include `.amazonq/rules/test-case-enhancement.md` in your LLM context
- Ask: "Enhance test cases for [problem_name] problem"

### 3. Improve Helper Classes

- Add new data structure helpers in `leetcode_py/data_structures/`
- Follow existing patterns with generic types and visualization support

### 4. Bug Fixes & Improvements

- Fix issues in existing problems
- Improve documentation
- Enhance CI/CD workflows

## Development Setup

```bash
git clone https://github.com/wisarootl/leetcode-py.git
cd leetcode-py
poetry install
make test
```

## Code Standards

- Follow [PEP 8](https://peps.python.org/pep-0008/) Python style guide
- Use modern type hints per [PEP 585](https://peps.python.org/pep-0585/)/[PEP 604](https://peps.python.org/pep-0604/): `list[str]`, `dict[str, int]`, `Type | None`
- Automated linting enforced by CI (black, isort, ruff, mypy)
- Minimum 12 test cases per problem

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `make lint` and `make test`
5. Submit a pull request with clear description

## Questions?

Open an issue for questions or discussions about contributions.
