# CLI Usage Guide

## Installation

```bash
pip install leetcode-py
```

## Quick Start

```bash
# Generate a single problem
lcpy gen -n 1

# Generate multiple problems
lcpy gen -n 1 -n 125 -n 206

# Generate by slug
lcpy gen -s two-sum -s valid-palindrome

# Generate all problems with a tag
lcpy gen -t grind-75

# List available problems
lcpy list

# Scrape problem data
lcpy scrape -n 1
```

## Commands

### `lcpy gen` - Generate Problems

Generate LeetCode problem templates from existing JSON definitions.

**Basic Usage:**

```bash
lcpy gen [OPTIONS]
```

**Options:**

- `-n, --problem-num` - Problem number(s) (use multiple -n flags)
- `-s, --problem-slug` - Problem slug(s) (use multiple -s flags)
- `-t, --problem-tag` - Problem tag for bulk generation
- `-d, --difficulty` - Filter by difficulty (Easy/Medium/Hard)
- `--all` - Generate all problems
- `-o, --output` - Output directory (default: current directory)
- `--force` - Force overwrite existing files

**Examples:**

```bash
# Single problem by number
lcpy gen -n 1

# Multiple problems by number
lcpy gen -n 1 -n 2 -n 3

# Single problem by slug
lcpy gen -s two-sum

# Multiple problems by slug
lcpy gen -s two-sum -s valid-palindrome

# All problems with specific tag (bulk generation)
lcpy gen -t grind-75

# Example: Generate all Grind 75 problems
lcpy gen --problem-tag grind-75 --output leetcode
```

![Problem Generation](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/problems-generation.png)

_Bulk generation output showing "Generated problem:" messages for all 75 Grind problems_

![Problem Generation 2](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/problems-generation-2.png)

_Generated folder structure showing all 75 problem directories after command execution_

```bash

# Filter by difficulty
lcpy gen -t grind-75 -d Easy

# Custom output directory
lcpy gen -n 1 -o my-problems

# Force overwrite existing files
lcpy gen -n 1 --force
```

### `lcpy scrape` - Scrape Problem Data

Fetch problem data from LeetCode and output as JSON.

**Basic Usage:**

```bash
lcpy scrape [OPTIONS]
```

**Options:**

- `-n, --problem-num` - Problem number
- `-s, --problem-slug` - Problem slug

**Examples:**

```bash
# Scrape by problem number
lcpy scrape -n 1

# Scrape by problem slug
lcpy scrape -s two-sum

# Save to file
lcpy scrape -n 1 > two_sum.json
```

### `lcpy list` - List Problems

Display available problems in a formatted table.

**Basic Usage:**

```bash
lcpy list [OPTIONS]
```

**Options:**

- `-t, --tag` - Filter by tag
- `-d, --difficulty` - Filter by difficulty

**Examples:**

```bash
# List all problems
lcpy list

# Filter by tag
lcpy list -t grind-75
lcpy list -t blind-75
lcpy list -t neetcode-150
lcpy list -t algo-master-75

# Filter by difficulty
lcpy list -d Easy

# Combine filters
lcpy list -t grind-75 -d Medium
lcpy list -t neetcode-150 -d Hard
```

## Problem Structure

Each generated problem creates the following structure:

```
problem_name/
├── README.md           # Problem description
├── solution.py         # Implementation template
├── test_solution.py    # Test cases
├── helpers.py          # Test helpers
├── playground.py       # Interactive debugging
└── __init__.py         # Package marker
```

![README Example](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/readme-example.png)

_README format that mirrors LeetCode's problem description layout_

![Solution Boilerplate](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/solution-boilerplate.png)

_Solution boilerplate with type hints and TODO placeholder_

![Test Example](https://raw.githubusercontent.com/wislertt/leetcode-py/main/docs/images/test-example.png)

_Comprehensive parametrized tests with 10+ test cases - executable and debuggable in local development environment_

## Tags

Available tags for bulk operations:

- `grind-75` - Essential 75 coding interview problems from [Grind 75](https://www.techinterviewhandbook.org/grind75/) ✅ Complete
- `grind` - Extended Grind collection (100+ problems) including all Grind 75 plus additional problems 🚧 Partial
- `blind-75` - Original [Blind 75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions) curated list 🚧 Partial
- `neetcode-150` - Comprehensive [NeetCode 150](https://neetcode.io/practice) problem set (150+ problems) 🚧 Partial
- `algo-master-75` - Curated algorithmic mastery problems (75 problems) 🚧 Partial

**Note**: Some problem sets are partially covered. We're actively working to complete all collections. [Contributions welcome!](https://github.com/wislertt/leetcode-py/blob/main/CONTRIBUTING.md)

## Output Directory

By default, problems are generated in the current directory. Use `-o` to specify a different location:

```bash
# Generate in current directory
lcpy gen -n 1

# Generate in specific directory
lcpy gen -n 1 -o leetcode

# Generate in absolute path
lcpy gen -n 1 -o /path/to/problems
```

## Error Handling

The CLI provides clear error messages and exit codes:

- **Exit code 0**: Success
- **Exit code 1**: Error occurred

**Common errors:**

- Problem number not found
- Invalid tag name
- File already exists (use `--force` to overwrite)
- Network errors during scraping

## Integration with Existing Workflow

The CLI is designed to work alongside the existing repository structure:

```bash
# In existing leetcode-py repository
lcpy gen -n 1 -o leetcode

# This creates: leetcode/two_sum/
```

## Tips

1. **Bulk Generation**: Use tags for efficient bulk operations
2. **Force Overwrite**: Use `--force` when regenerating existing problems
3. **Output Organization**: Use `-o` to organize problems in subdirectories
4. **Filtering**: Combine tags and difficulty filters for precise selection
5. **Scripting**: CLI commands work well in shell scripts and automation
