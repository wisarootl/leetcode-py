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

### Prerequisites

- **Python 3.10+** - Modern Python runtime
- **Poetry** - Dependency management ([install guide](https://python-poetry.org/docs/#installation))
- **Make** - Build automation (usually pre-installed on Unix systems)
- **Git** - Version control
- **Graphviz** - Graph visualization ([install guide](https://graphviz.org/download/))

## Development Workflow

### 1. Fork and Setup

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/leetcode-py.git
cd leetcode-py
poetry install

# Add upstream remote
git remote add upstream https://github.com/wisarootl/leetcode-py.git

# Verify setup
make test
make lint
```

### 2. Create Feature Branch

```bash
git checkout -b your-feature-name
```

### 3. Make Changes and Test

```bash
# Test specific problem
make p-test PROBLEM=problem_name

# Test all
make test

# Lint your changes
make lint

# Generate/regenerate problems (if needed)
make p-gen PROBLEM=problem_name
```

### 4. Submit Pull Request

```bash
# Commit and push to your fork
git add .
git commit -m "feat: your descriptive commit message"
git push origin your-feature-name

# Then create a pull request on GitHub from your fork to the main repository
```

**Ensure all GitHub Actions CI checks pass before requesting review.**

## Questions?

Open an issue for questions or discussions about contributions.
