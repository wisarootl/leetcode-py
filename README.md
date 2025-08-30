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
- **Beautiful tree visualizations** - Pretty-printed binary trees with anytree
- **Rich test logging** - `@logged_test` decorator with detailed tracebacks
- **One-command testing** - `make test-question QUESTION=problem_name`
- **Code quality** - black, isort, ruff, mypy integration
- **Modern Python** - PEP 585/604 syntax with full type hints

## 🚀 Quick Start

```bash
# Run existing problems
make q-test QUESTION=two_sum
make q-test QUESTION=invert_binary_tree

# Run all tests
make test
```

**Adding new problems**: Use an LLM agent (rules in `.amazonq/rules/development-rules.md`) to automatically create new problems from copied LeetCode problem text using the template structure.

## 🧰 Commands

```bash
make q-test QUESTION=two_sum  # Test specific problem
make test                     # Run all tests
make lint                     # Code quality checks
make q-gen QUESTION=new_prob  # Generate new problem
```

## 🎨 Example Output

```
# TreeNode visualization
4
├── 2
│   ├── 1
│   └── 3
└── 7
    ├── 6
    └── 9

# Test logging
2024-01-01 10:00:00 | SUCCESS | Got result: [4,7,2,9,6,3,1]
2024-01-01 10:00:00 | DEBUG   | Test passed! ✨
```

Perfect for interview preparation with professional-grade tooling and beautiful visualizations.
