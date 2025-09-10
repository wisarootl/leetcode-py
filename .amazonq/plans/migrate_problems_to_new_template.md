# Migrate Problems to New Template Format

## Overview

Migrate all problems from old JSON format (`.templates/leetcode/json_old/`) to new template format (`.templates/leetcode/json/`) one by one.

## Prerequisites

- New template system is ready in `.templates/leetcode/{{cookiecutter.problem_name}}/`
- Helper script exists: `.amazonq/plans/find_next_problem.py`

## Process

### Step 1: Find Next Problem

```bash
python .amazonq/plans/find_next_problem.py
```

This returns the next problem to migrate (e.g., `accounts_merge`).

### Step 2: Analyze Old JSON

```bash
# Check the old format
cat .templates/leetcode/json_old/accounts_merge.json
```

Understand the structure and required variables.

### Step 3: Create New JSON

Create `.templates/leetcode/json/accounts_merge.json` with new template variables:

**Required Variables:**

- `problem_name` - Snake case name
- `solution_class_name` - Usually "Solution"
- `problem_number` - LeetCode number
- `problem_title` - Exact title
- `difficulty` - Easy/Medium/Hard
- `topics` - Comma-separated topics

**Template-Specific Variables:**

- `helpers_imports` - Imports for helpers.py
- `helpers_content` - Helper functions
- `helpers_run_name` - Main method name
- `helpers_run_signature` - Method signature
- `helpers_run_body` - Method implementation
- `helpers_assert_name` - Assert function name
- `helpers_assert_signature` - Assert signature
- `helpers_assert_body` - Assert implementation
- `solution_imports` - Imports for solution.py
- `solution_class_content` - Class-level content
- `solution_methods` - Array of method objects
- `test_imports` - Test imports
- `test_methods` - Array of test method objects
- `playground_imports` - Notebook imports
- `playground_setup` - Test case setup
- `playground_run` - Execution code
- `playground_assert` - Assertion code
- `readme_description` - Problem description
- `readme_constraints` - Constraints

### Step 4: Generate and Test

```bash
# Generate problem structure
make p-gen PROBLEM=accounts_merge

# Lint to catch issues
make p-lint PROBLEM=accounts_merge

# Fix any linting errors by updating JSON or generated files
```

### Step 5: Verify Generation

Check generated files:

- `leetcode/accounts_merge/README.md`
- `leetcode/accounts_merge/solution.py`
- `leetcode/accounts_merge/helpers.py`
- `leetcode/accounts_merge/test_solution.py`
- `leetcode/accounts_merge/playground.ipynb`

### Step 6: Implement Solution

```bash
# Copy implementation from old repository
# Find the solution in leetcode_old/ and implement in solution.py
# Replace TODO with actual working solution
```

### Step 7: Test Functionality

```bash
# Run tests to ensure everything works
make p-test PROBLEM=accounts_merge
```

### Step 8: Repeat

```bash
# Find next problem
python .amazonq/plans/find_next_problem.py
```

Repeat process until script returns "All problems updated!"

## Migration Checklist

For each problem:

- [ ] Run `find_next_problem.py` to get next problem
- [ ] Analyze old JSON structure
- [ ] Create new JSON with all required variables
- [ ] Run `make p-gen PROBLEM=<name>`
- [ ] Run `make p-lint PROBLEM=<name>` and fix issues:
    - If linting fails, fix the JSON template
    - Re-run `make p-gen PROBLEM=<name> FORCE=1` to regenerate
    - Re-run `make p-lint PROBLEM=<name>` to verify
    - Iterate until linting passes to ensure reproducibility
- [ ] Implement solution from `leetcode_old/` repository
- [ ] Run `make p-test PROBLEM=<name>` to verify tests pass
- [ ] Commit changes

## Common Patterns

**Basic Problem:**

```json
{
    "problem_name": "two_sum",
    "solution_class_name": "Solution",
    "helpers_run_name": "two_sum",
    "helpers_run_signature": "(solution_class: type, nums: list[int], target: int)",
    "helpers_run_body": "return solution_class().two_sum(nums, target)",
    "solution_methods": [
        {
            "name": "two_sum",
            "signature": "(self, nums: list[int], target: int) -> list[int]",
            "body": "# TODO: Implement\nreturn []"
        }
    ]
}
```

**Tree Problem:**

```json
{
    "helpers_imports": "from leetcode_py import TreeNode",
    "helpers_content": "def create_tree(root_list: list[int | None]) -> TreeNode[int] | None:\n    return TreeNode[int].from_list(root_list)",
    "solution_imports": "from leetcode_py import TreeNode"
}
```

**Design Problem:**

```json
{
    "solution_class_name": "LRUCache",
    "solution_methods": [
        {
            "name": "__init__",
            "signature": "(self, capacity: int)",
            "body": "# TODO: Initialize"
        },
        {
            "name": "get",
            "signature": "(self, key: int) -> int",
            "body": "# TODO: Implement\nreturn -1"
        }
    ]
}
```

## Progress Tracking

Track progress by running the script periodically:

```bash
# Check remaining problems
ls .templates/leetcode/json_old/ | wc -l  # Total old problems
ls .templates/leetcode/json/ | wc -l      # Migrated problems
python .amazonq/plans/find_next_problem.py # Next to migrate
```

## Completion

When `find_next_problem.py` returns "All problems updated!", the migration is complete.
