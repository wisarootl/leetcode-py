# Contributing to LeetCode Practice Repository

Thank you for your interest in contributing! This repository welcomes contributions from the community.

## Ways to Contribute

### 1. Add New Problems

For adding new LeetCode problems, please refer to the comprehensive guide:

📖 **[LLM-Assisted Problem Creation Guide](docs/llm-assisted-problem-creation.md)**

This document provides detailed instructions for using LLM assistants to generate new problems with proper templates, test cases, and documentation.

**Acceptance Criteria:**

- All GitHub Actions CI checks must pass (includes linting, testing, security scanning, reproducibility verification, and minimum 10 test cases per problem)
- Proper type hints and code formatting
- Complete the solution (documentation is auto-generated)

### 2. Other Contributions

All other contributions are welcome! This includes:

- Bug fixes and improvements
- Documentation enhancements
- Helper class improvements
- CI/CD workflow enhancements
- Test case enhancements
- New data structure visualizations

**For small changes:** Feel free to open a pull request directly.

**For larger changes:** Please open an issue for discussion first.

I'm also open to feedback and suggestions for improving the project!

## Development Setup

```bash
git clone https://github.com/wisarootl/leetcode-py.git
cd leetcode-py
poetry install
make test
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `make lint` and `make test`
5. Ensure all GitHub Actions CI checks pass
6. Submit a pull request with clear description

## Questions?

Open an issue for questions or discussions about contributions.
