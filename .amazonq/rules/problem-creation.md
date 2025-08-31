# Problem Creation Guide

## Assistant Workflow

When user requests a problem by **number** or **name/slug**, the assistant will:

1. **Scrape** problem data using `.templates/leetcode/scrape.py`
2. **Transform** data into proper JSON template format
3. **Create** JSON file in `.templates/leetcode/json/{problem_name}.json`
4. **Update** Makefile with `PROBLEM ?= {problem_name}`
5. **Generate** problem structure using `make p-gen`
6. **Verify** with `make lint` - fix template issues in JSON if possible, or manually fix generated files if template limitations
7. **Iterate** if JSON fixes: re-run `make p-gen PROBLEM={problem_name} FORCE=1` and `make lint` until passes to ensure reproducibility

## Scraping Commands

```bash
# Fetch by number
poetry run python .templates/leetcode/scrape.py -n 1

# Fetch by slug
poetry run python .templates/leetcode/scrape.py -s "two-sum"
```

## JSON Template Format

Required fields for `.templates/leetcode/json/{problem_name}.json`:

**Reference examples in `.templates/leetcode/examples/` for complete templates:**

- `basic.json5` - Array, string, number problems
- `tree.json5` - Binary tree problems
- `linked_list.json5` - Linked list problems
- `string.json5` - String manipulation problems
- `matrix.json5` - 2D array/matrix problems

```json
{
    "problem_name": "two_sum",
    "class_name": "TwoSum",
    "method_name": "two_sum",
    "problem_number": "1",
    "problem_title": "Two Sum",
    "difficulty": "Easy",
    "topics": "Array, Hash Table",
    "tags": ["grind-75"],
    "problem_description": "Given an array...",
    "examples": [{ "input": "nums = [2,7,11,15], target = 9", "output": "[0,1]" }],
    "constraints": "- 2 <= nums.length <= 10^4",
    "parameters": "nums: list[int], target: int",
    "return_type": "list[int]",
    "dummy_return": "[]",
    "imports": "",
    "test_cases": [{ "args": [[2, 7, 11, 15], 9], "expected": [0, 1] }],
    "param_names": "nums, target, expected",
    "param_names_with_types": "nums: list[int], target: int, expected: list[int]",
    "input_description": "nums={nums}, target={target}",
    "input_params": "nums, target",
    "expected_param": "expected",
    "method_args": "nums, target",
    "test_setup": "",
    "test_logging": "",
    "assertion_code": "assert result == expected",
    "test_input_setup": "nums = [2, 7, 11, 15]\ntarget = 9",
    "expected_output_setup": "expected = [0, 1]"
}
```

## Naming Conventions

- **problem_name**: snake_case (e.g., "two_sum", "valid_palindrome")
- **class_name**: PascalCase (e.g., "TwoSum", "ValidPalindrome")
- **method_name**: snake_case (e.g., "two_sum", "is_palindrome")
- **parameters**: Use snake_case for all parameter names

## Special Problem Types

### Tree Problems

- Add `"imports": "from leetcode_py.tree_node import TreeNode"`
- Use `TreeNode | None` for nullable tree parameters
- Test setup: `root = TreeNode.from_list(root_list)`

### Linked List Problems

- Add `"imports": "from leetcode_py.list_node import ListNode"`
- Use `ListNode | None` for nullable list parameters
- Test setup: `head = ListNode.from_list(head_list)`

## Generation Commands

```bash
# Generate problem
make p-gen PROBLEM={problem_name}

# Force regenerate (if files exist)
make p-gen PROBLEM={problem_name} FORCE=1

# Test specific problem
make p-test PROBLEM={problem_name}

# Lint check
make lint
```

## Tags (Optional)

Common tags: `["grind-75", "blind-75", "neetcode-150", "top-interview"]`
