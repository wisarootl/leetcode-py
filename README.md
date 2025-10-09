# LeetCode Practice Environment Generator 🚀

[![tests](https://img.shields.io/github/actions/workflow/status/wislertt/leetcode-py/ci-test.yml?branch=main&label=tests&logo=github)](https://github.com/wislertt/leetcode-py/actions/workflows/ci-test.yml)
[![release](https://img.shields.io/github/actions/workflow/status/wislertt/leetcode-py/cd.yml?branch=main&label=release&logo=github)](https://github.com/wislertt/leetcode-py/actions/workflows/cd.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wislertt_leetcode-py&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wislertt_leetcode-py)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=wislertt_leetcode-py&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=wislertt_leetcode-py)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=wislertt_leetcode-py&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=wislertt_leetcode-py)
[![codecov](https://codecov.io/gh/wislertt/leetcode-py/graph/badge.svg?token=TI97VUIA4Z)](https://codecov.io/gh/wislertt/leetcode-py)
[![pypi](https://img.shields.io/pypi/v/leetcode-py-sdk.svg?color=blue)](https://pypi.python.org/pypi/leetcode-py-sdk)
[![downloads](https://static.pepy.tech/personalized-badge/leetcode-py-sdk?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads)](https://pepy.tech/projects/leetcode-py-sdk)
[![python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue?logo=python)](https://github.com/wislertt/leetcode-py/)
[![Star ⭐](https://img.shields.io/github/stars/wislertt/leetcode-py?style=flat&logo=github&color=ffcc00)](https://github.com/wislertt/leetcode-py)
[![Sponsor 💖](https://img.shields.io/badge/Sponsor-💖-pink?style=flat)](https://github.com/sponsors/wislertt)

A Python package to generate professional LeetCode practice environments. Features automated problem generation from LeetCode URLs, beautiful data structure visualizations (TreeNode, ListNode, GraphNode), and comprehensive testing with 10+ test cases per problem. Built with professional development practices including CI/CD, type hints, and quality gates.

## Table of Contents

- [What's Included](#whats-included)
- [Quick Start](#quick-start)
- [Problem Structure](#problem-structure)
- [Key Features](#key-features)
- [Usage Patterns](#usage-patterns)
- [Development Setup](#development-setup)
- [Helper Classes](#helper-classes)
- [Commands](#commands)
- [Architecture](#architecture)
- [Quality Metrics](#quality-metrics)

**What makes this different:**

- 🤖 **[LLM-Assisted Workflow](https://github.com/wislertt/leetcode-py/blob/main/docs/llm-assisted-problem-creation.md)**: Generate new problems instantly with AI assistance
- 🎨 **Visual Debugging**: Interactive tree/graph rendering with Graphviz and anytree
- 🧪 **Production Testing**: Comprehensive test suites with edge cases and reproducibility verification
- 🚀 **Modern Python**: PEP 585/604 type hints, Poetry, and professional tooling
- 📊 **Quality Assurance**: 95%+ test coverage, security scanning, automated linting
- ⚡ **[Powerful CLI](https://github.com/wislertt/leetcode-py/blob/main/docs/cli-usage.md)**: Generate problems anywhere with `lcpy` command

## <a id="whats-included"></a>🎯 What's Included

**Current Problem Sets**:

- **grind-75** - Essential coding interview questions from [Grind 75](https://www.techinterviewhandbook.org/grind75/) ✅ Complete
- **grind** - Extended Grind collection including all Grind 75 plus additional problems 🚧 Partial
- **blind-75** - Original [Blind 75](https://leetcode.com/problem-list/xi4ci4ig/) curated list 🚧 Partial
- **neetcode-150** - Comprehensive [NeetCode 150](https://neetcode.io/practice) problem set 🚧 Partial
- **algo-master-75** - Curated algorithmic mastery problems 🚧 Partial

**Coverage**: 120+ unique problems across all major coding interview topics and difficulty levels.

**Note**: Some problem sets are partially covered. We're actively working to complete all collections. [Contributions welcome!](https://github.com/wislertt/leetcode-py/blob/main/CONTRIBUTING.md)

## <a id="quick-start"></a>🚀 Quick Start

### System Requirements

- **Python 3.10+** - Python runtime
- **Graphviz** - Graph visualization library ([install guide](https://graphviz.org/download/))

```bash
# Install the package
pip install leetcode-py-sdk

# Generate problems anywhere
lcpy gen -n 1                    # Generate Two Sum
lcpy gen -t grind-75             # Generate all Grind 75 problems
lcpy gen -t neetcode-150         # Generate NeetCode 150 problems
lcpy list -t grind-75            # List Grind 75 problems
lcpy list -t blind-75            # List Blind 75 problems

# Start practicing
cd leetcode/two_sum
python -m pytest test_solution.py  # Run tests
# Edit solution.py, then rerun tests
```

### Bulk Generation Example

```bash
lcpy gen --problem-tag grind-75 --output leetcode     # Generate all Grind 75 problems
lcpy gen --problem-tag neetcode-150 --output leetcode   # Generate NeetCode 150 problems
lcpy gen --problem-tag blind-75 --output leetcode       # Generate Blind 75 problems
```

![Problem Generation](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/problems-generation.png)

_Bulk generation output showing "Generated problem:" messages for all 75 Grind problems_

![Problem Generation 2](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/problems-generation-2.png)

_Generated folder structure showing all 75 problem directories after command execution_

## <a id="problem-structure"></a>📁 Problem Structure

Each problem follows a consistent, production-ready template:

```
leetcode/two_sum/
├── README.md           # Problem description with examples and constraints
├── solution.py         # Implementation with type hints and TODO placeholder
├── test_solution.py    # Comprehensive parametrized tests (10+ test cases)
├── helpers.py          # Test helper functions
├── playground.py       # Interactive debugging environment (converted from .ipynb)
└── __init__.py         # Package marker
```

![README Example](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/readme-example.png)

_README format that mirrors LeetCode's problem description layout_

![Solution Boilerplate](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/solution-boilerplate.png)

_Solution boilerplate with type hints and TODO placeholder_

![Test Example](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/test-example.png)

_Comprehensive parametrized tests with 10+ test cases - executable and debuggable in local development environment_

![Test Logging](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/logs-in-test-solution.png)

_Beautiful colorful test output with loguru integration for enhanced debugging and test result visualization_

## <a id="key-features"></a>✨ Key Features

### Production-Grade Development Environment

- **Modern Python**: PEP 585/604 type hints, snake_case conventions
- **Comprehensive Linting**: black, isort, ruff, mypy with nbqa for notebooks
- **High Test Coverage**: 10+ test cases per problem including edge cases
- **Beautiful Logging**: loguru integration for enhanced test debugging
- **CI/CD Pipeline**: Automated testing, security scanning, and quality gates

### Enhanced Data Structure Visualization

Professional-grade visualization for debugging complex data structures with dual rendering modes:

- **TreeNode**: Beautiful tree rendering with anytree and Graphviz integration
- **ListNode**: Clean arrow-based visualization with cycle detection
- **GraphNode**: Interactive graph rendering for adjacency list problems
- **DictTree**: Box-drawing character trees perfect for Trie implementations

#### Jupyter Notebook Integration (HTML Rendering)

![Tree Visualization](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/tree-viz.png)

_Interactive tree visualization using Graphviz SVG rendering in Jupyter notebooks_

![LinkedList Visualization](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/linkedlist-viz.png)

_Professional linked list visualization with Graphviz in Jupyter environment_

#### Terminal/Console Output (String Rendering)

![Tree String Visualization](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/tree-str-viz.png)

_Clean ASCII tree rendering using anytree for terminal debugging and logging_

![LinkedList String Visualization](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/linkedlist-str-viz.png)

_Simple arrow-based list representation for console output and test debugging_

### Flexible Notebook Support

- **Template Generation**: Creates Jupyter notebooks (`.ipynb`) by default with rich data structure rendering
- **User Choice**: Use `jupytext` to convert notebooks to Python files, or keep as `.ipynb` for interactive exploration
- **Repository State**: This repo converts them to Python files (`.py`) for better version control
- **Dual Rendering**: Automatic HTML visualization in notebooks, clean string output in terminals

![Notebook Example](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/notebook-example.png)

_Interactive multi-cell playground with rich data structure visualization for each problem_

## <a id="usage-patterns"></a>🔄 Usage Patterns

### CLI Usage (Global Installation)

Perfect for quick problem generation anywhere. See the 📖 **[Complete CLI Usage Guide](https://github.com/wislertt/leetcode-py/blob/main/docs/cli-usage.md)** for detailed documentation with all options and examples.

## <a id="development-setup"></a>🛠️ Development Setup

For working within this repository to generate additional LeetCode problems using LLM assistance:

### Development Requirements

- **Python 3.10+** - Modern Python runtime with latest type system features
- **Poetry** - Dependency management and packaging
- **Make** - Build automation (development workflows)
- **Git** - Version control system
- **Graphviz** - Graph visualization library ([install guide](https://graphviz.org/download/))

```bash
# Clone repository for development
git clone https://github.com/wislertt/leetcode-py.git
cd leetcode-py
poetry install

# Generate problems from JSON templates
make p-gen PROBLEM=problem_name
make p-test PROBLEM=problem_name

# Regenerate all existing problems
make gen-all-problems
```

### LLM-Assisted Problem Creation

To extend the problem collection beyond the current catalog, leverage an LLM assistant within your IDE (Cursor, GitHub Copilot Chat, Amazon Q, etc.).

📖 **[Complete LLM-Assisted Problem Creation Guide](https://github.com/wislertt/leetcode-py/blob/main/docs/llm-assisted-problem-creation.md)** - Comprehensive guide with screenshots and detailed workflow.

**Quick Start:**

```bash
# Problem generation commands:
"Add problem 198. House Robber"
"Add problem 198. House Robber. tag: grind"

# Test enhancement commands:
"Enhance test cases for two_sum problem"
"Fix test reproducibility for binary_tree_inorder_traversal"
```

**Required LLM Context**: Include these rule files in your LLM context for automated problem generation and test enhancement:

- [`.cursor/commands/problem-creation.md`](https://github.com/wislertt/leetcode-py/blob/main/.cursor/commands/problem-creation.md) - Complete problem generation workflow
- [`.cursor/commands/test-quality-assurance.md`](https://github.com/wislertt/leetcode-py/blob/main/.cursor/commands/test-quality-assurance.md) - Test enhancement and reproducibility verification

**Manual Check**: Find problems needing more test cases:

```bash
poetry run python -m leetcode_py.tools.check_test_cases --threshold=10
```

## 🧰 Helper Classes

- **TreeNode**: `from leetcode_py import TreeNode`
    - Array ↔ tree conversion: `TreeNode.from_list([1,2,3])`, `tree.to_list()`
    - Beautiful anytree text rendering and Graphviz SVG for Jupyter
    - Node search: `tree.find_node(value)`
    - Generic type support: `TreeNode[int]`, `TreeNode[str]`

- **ListNode**: `from leetcode_py import ListNode`
    - Array ↔ list conversion: `ListNode.from_list([1,2,3])`, `node.to_list()`
    - Cycle detection with Floyd's algorithm
    - Graphviz visualization for Jupyter notebooks
    - Generic type support: `ListNode[int]`, `ListNode[str]`

- **GraphNode**: `from leetcode_py import GraphNode`
    - Adjacency list conversion: `GraphNode.from_adjacency_list([[2,4],[1,3],[2,4],[1,3]])`
    - Clone detection: `original.is_clone(cloned)`
    - Graphviz visualization for undirected graphs
    - DFS traversal utilities

- **DictTree**: `from leetcode_py.data_structures import DictTree`
    - Perfect for Trie implementations: `DictTree[str]()`
    - Beautiful tree rendering with box-drawing characters
    - Graphviz visualization for Jupyter notebooks
    - Generic key type support

## 🛠️ Commands

### CLI Commands (Global)

📖 **[Complete CLI Usage Guide](https://github.com/wislertt/leetcode-py/blob/main/docs/cli-usage.md)** - Detailed documentation with all options and examples.

```bash
# Generate problems
lcpy gen -n 1                       # Single problem by number
lcpy gen -s two-sum                 # Single problem by slug
lcpy gen -t grind-75                # Bulk generation by tag
lcpy gen -t neetcode-150            # Generate NeetCode 150 problems
lcpy gen -n 1 -n 2 -n 3            # Multiple problems
lcpy gen -t grind-75 -d Easy       # Filter by difficulty
lcpy gen -n 1 -o my-problems       # Custom output directory

# List problems
lcpy list                           # All available problems
lcpy list -t grind-75               # Filter by Grind 75 tag
lcpy list -t blind-75               # Filter by Blind 75 tag
lcpy list -t neetcode-150           # Filter by NeetCode 150 tag
lcpy list -d Medium                 # Filter by difficulty

# Scrape problem data
lcpy scrape -n 1                   # Fetch by number
lcpy scrape -s two-sum             # Fetch by slug
```

### Development Commands (Repository)

```bash
# Problem-specific operations
make p-test PROBLEM=problem_name    # Test specific problem
make p-gen PROBLEM=problem_name     # Generate problem from JSON template
make p-lint PROBLEM=problem_name    # Lint specific problem

# Bulk operations
make test                           # Run all tests
make lint                           # Lint entire codebase
make gen-all-problems              # Regenerate all problems (destructive)
```

## 🏗️ Architecture

- **Template-Driven**: JSON templates in `.templates/leetcode/json/` drive code generation
- **Cookiecutter Integration**: Uses `.templates/leetcode/{{cookiecutter.problem_name}}/` template for consistent file structure
- **Automated Scraping**: LLM-assisted problem data extraction from LeetCode
- **Version Control Friendly**: Python files by default, optional notebook support

## 📊 Quality Metrics

- **Test Coverage**: 95%+ with comprehensive edge case testing (Codecov integration)
- **Security**: SonarCloud quality gates, Trivy dependency scanning, Gitleaks secret detection
- **Code Quality**: Automated linting with black, isort, ruff, mypy
- **Test Reproducibility**: Automated verification that problems can be regenerated consistently
- **CI/CD**: GitHub Actions for testing, security, pre-commit hooks, and release automation

Perfect for systematic coding interview preparation with professional development practices and enhanced debugging capabilities.

## 💖 Support This Project

[![Star ⭐](https://img.shields.io/github/stars/wislertt/leetcode-py?style=flat&logo=github&color=ffcc00)](https://github.com/wislertt/leetcode-py)
[![Sponsor 💖](https://img.shields.io/badge/Sponsor-💖-pink?style=flat)](https://github.com/sponsors/wislertt)

If you find this project helpful, please consider **starring the repo ⭐** or **sponsoring my work 💖**.
Your support helps me maintain and improve this project. Thank you!
