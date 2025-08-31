# LeetCode Practice Repository 🚀

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wisarootl_leetcode-py&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wisarootl_leetcode-py)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=wisarootl_leetcode-py&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=wisarootl_leetcode-py)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=wisarootl_leetcode-py&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=wisarootl_leetcode-py)
[![codecov](https://codecov.io/gh/wisarootl/leetcode-py/graph/badge.svg?token=TI97VUIA4Z)](https://codecov.io/gh/wisarootl/leetcode-py)
[![tests](https://img.shields.io/github/actions/workflow/status/wisarootl/leetcode-py/ci-test.yml?branch=main&label=tests&logo=github)](https://github.com/wisarootl/zerv/actions/workflows/ci-test.yml)
[![release](https://img.shields.io/github/actions/workflow/status/wisarootl/leetcode-py/cd.yml?branch=main&label=release&logo=github)](https://github.com/wisarootl/zerv/actions/workflows/cd.yml)

Premium LeetCode practice repository with Python solutions, algorithm templates, data structure visualizations, and automated testing. Perfect for coding interview preparation, competitive programming, and mastering algorithms with Blind 75, Grind 75, and NeetCode 150 problems.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/wisarootl/leetcode-py.git
cd leetcode-py

# Install dependencies
poetry install

# Generate all problems to start practicing (fresh start - wipes all solutions)
make gen-all-problems

# Run existing problems
make p-test PROBLEM=insert_interval
make p-test PROBLEM=invert_binary_tree

# Run all tests
make test
```

## 📋 Prerequisites

- Python 3.13+
- make, git, Graphviz, poetry

## 📁 Problem Structure

Each problem follows a consistent template:

```
leetcode/two_sum/
├── README.md          # Problem description and examples
├── solution.py        # Your implementation with TODO placeholder
├── tests.py          # Comprehensive test cases
├── notebook.ipynb    # Interactive playground
└── __init__.py       # Package marker
```

## 🎯 Supported Problem Categories

- **Arrays & Hashing** - Two Sum, Group Anagrams, Top K Elements
- **Two Pointers** - Valid Palindrome, Container With Most Water
- **Sliding Window** - Longest Substring, Minimum Window
- **Stack** - Valid Parentheses, Daily Temperatures
- **Binary Search** - Search Rotated Array, Find Minimum
- **Linked Lists** - Reverse List, Merge Lists, Detect Cycle
- **Trees** - Invert Tree, Maximum Depth, Serialize/Deserialize
- **Tries** - Implement Trie, Word Search II
- **Heap/Priority Queue** - Merge K Lists, Find Median
- **Backtracking** - Combination Sum, Word Search, N-Queens
- **Graphs** - Clone Graph, Course Schedule, Islands
- **Advanced DP** - Climbing Stairs, Coin Change, LCS
- **Greedy** - Jump Game, Gas Station
- **Intervals** - Merge Intervals, Meeting Rooms
- **Math & Geometry** - Rotate Image, Spiral Matrix

Includes problems from **Blind 75**, **Grind 75**, **NeetCode 150**, and **Top Interview Questions**. This is an ongoing project - contributions are welcome!

## 🎨 Visualizations

### Tree Visualization

![Tree Visualization Placeholder](docs/images/tree-viz.png)
_Beautiful tree rendering with anytree and Graphviz_

### Linked List Visualization

![LinkedList Visualization Placeholder](docs/images/linkedlist-viz.png)
_Clean arrow-based list visualization_

### Jupyter Notebook Integration

![Notebook Placeholder](docs/images/notebook-example.png)
_Interactive multi-cell playground for each problem_

## ✨ Features

- **Template-driven development** - Consistent structure for every problem
- **Beautiful visualizations** - TreeNode with anytree/Graphviz, ListNode with arrows
- **Interactive notebooks** - Multi-cell playground for each problem
- **One-command testing** - `make p-test PROBLEM=problem_name`
- **Bulk regeneration** - `make gen-all-problems` from JSON templates
- **Full linting** - black, isort, ruff, mypy with nbqa for notebooks
- **Modern Python** - PEP 585/604 syntax with full type hints

## 🔄 Workflow Examples

**Practice existing problems**:

```bash
# Work on a specific problem
make p-test PROBLEM=two_sum
# Edit leetcode/two_sum/solution.py
# Run tests to verify
```

**Add new problems**:

```bash
# Ask your LLM assistant:
# "Create LeetCode problem 146 (LRU Cache)"
# The assistant handles everything automatically!
```

_Behind the scenes: Assistant follows `.amazonq/rules/problem-creation.md` to scrape problem data, create JSON template, generate structure with `make p-gen`, and verify with `make lint`._

**Bulk operations**:

```bash
# Test all problems
make test
# Regenerate all from templates
make gen-all-problems
# Check code quality
make lint
```

## 🧰 Helper Classes

- **TreeNode**: `from leetcode_py import TreeNode`
    - Beautiful tree visualization with anytree rendering
    - Jupyter notebook support with Graphviz diagrams
    - Easy array ↔ tree conversion for testing
- **ListNode**: `from leetcode_py import ListNode`
    - Clean arrow visualization (`1 -> 2 -> 3`)
    - Simple array ↔ list conversion
    - Perfect for debugging linked list problems
- New helpers: Add to `leetcode_py/`

This is an ongoing project - contributions are welcome!

Perfect for interview preparation with professional-grade tooling and beautiful visualizations.
