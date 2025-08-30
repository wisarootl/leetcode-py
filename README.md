# LeetCode Practice Repository 🚀

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wisarootl_leetcode-py&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wisarootl_leetcode-py)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=wisarootl_leetcode-py&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=wisarootl_leetcode-py)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=wisarootl_leetcode-py&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=wisarootl_leetcode-py)
[![codecov](https://codecov.io/gh/wisarootl/leetcode-py/graph/badge.svg?token=TI97VUIA4Z)](https://codecov.io/gh/wisarootl/leetcode-py)
[![tests](https://img.shields.io/github/actions/workflow/status/wisarootl/leetcode-py/ci-test.yml?branch=main&label=tests&logo=github)](https://github.com/wisarootl/zerv/actions/workflows/ci-test.yml)
[![release](https://img.shields.io/github/actions/workflow/status/wisarootl/leetcode-py/cd.yml?branch=main&label=release&logo=github)](https://github.com/wisarootl/zerv/actions/workflows/cd.yml)

Premium LeetCode practice environment with modern Python tooling, beautiful tree visualizations, and comprehensive testing.

## ✨ Features

- **Template-driven development** - Consistent structure for every problem
- **Beautiful visualizations** - TreeNode with anytree/Graphviz, ListNode with arrows
- **Interactive notebooks** - Multi-cell playground for each problem
- **One-command testing** - `make q-test QUESTION=problem_name`
- **Bulk regeneration** - `make gen-all-questions` from JSON templates
- **Full linting** - black, isort, ruff, mypy with nbqa for notebooks
- **Modern Python** - PEP 585/604 syntax with full type hints

## 🚀 Quick Start

```bash
# Run existing problems
make q-test QUESTION=insert_interval
make q-test QUESTION=invert_binary_tree

# Run all tests
make test
```

**Adding new problems**:

- Copy question and placeholder solution from LeetCode
- Ask LLM to generate them
- LLM follows workflow in `.amazonq/rules/question-creation.md` using cookiecutter templates

## 🧰 Commands

```bash
make q-test QUESTION=insert_interval    # Test specific problem
make test                               # Run all tests
make lint                               # Code quality checks
make q-gen QUESTION=new_prob            # Generate new problem
```

**🍴 Fork Setup**:

```bash
make gen-all-questions                  # Regenerate all problems from JSON templates
```

## 🧰 Helper Classes

- **TreeNode**: `from leetcode_py.tree_node import TreeNode`
    - Beautiful tree visualization with anytree rendering
    - Jupyter notebook support with Graphviz diagrams
    - Easy array ↔ tree conversion for testing
- **ListNode**: `from leetcode_py.list_node import ListNode`
    - Clean arrow visualization (`1 -> 2 -> 3`)
    - Simple array ↔ list conversion
    - Perfect for debugging linked list problems
- New helpers: Add to `leetcode_py/`

Perfect for interview preparation with professional-grade tooling and beautiful visualizations.
