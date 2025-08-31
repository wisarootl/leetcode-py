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
- `design.json5` - Data structure design problems (LRU Cache, etc.)
- `tree.json5` - Binary tree problems
- `linked_list.json5` - Linked list problems
- `matrix.json5` - 2D array/matrix problems

````json
{
    "problem_name": "two_sum",
    "solution_class_name": "Solution",
    "problem_number": "1",
    "problem_title": "Two Sum",
    "difficulty": "Easy",
    "topics": "Array, Hash Table",
    "tags": ["grind-75"],
    "readme_description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
    "readme_examples": [
        {
            "content": "```\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\n```\n**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]."
        }
    ],
    "readme_constraints": "- 2 <= nums.length <= 10^4\n- -10^9 <= nums[i] <= 10^9\n- -10^9 <= target <= 10^9\n- Only one valid answer exists.",
    "readme_additional": "",
    "solution_imports": "",
    "solution_methods": [
        {
            "name": "two_sum",
            "parameters": "nums: list[int], target: int",
            "return_type": "list[int]",
            "dummy_return": "[]"
        }
    ],
    "test_imports": "import pytest\nfrom leetcode_py.test_utils import logged_test\nfrom .solution import Solution",
    "test_class_name": "TwoSum",
    "test_helper_methods": [
        {
            "name": "setup_method",
            "parameters": "",
            "body": "self.solution = Solution()"
        }
    ],
    "test_methods": [
        {
            "name": "test_two_sum",
            "parametrize": "nums, target, expected",
            "parametrize_typed": "nums: list[int], target: int, expected: list[int]",
            "test_cases": "[([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2])]",
            "body": "result = self.solution.two_sum(nums, target)\nassert result == expected"
        }
    ],
    "playground_imports": "from solution import Solution",
    "playground_test_case": "# Example test case\nnums = [2, 7, 11, 15]\ntarget = 9\nexpected = [0, 1]",
    "playground_execution": "result = Solution().two_sum(nums, target)\nresult",
    "playground_assertion": "assert result == expected"
}
````

## Naming Conventions

- **problem_name**: snake_case (e.g., "two_sum", "valid_palindrome")
- **solution_class_name**: Usually "Solution", except for design problems (e.g., "LRUCache")
- **test_class_name**: PascalCase (e.g., "TwoSum", "ValidPalindrome")
- **method_name**: snake_case (e.g., "two_sum", "is_palindrome")
- **parameters**: Use snake_case for all parameter names

## Special Problem Types

### Tree Problems

- Add `"solution_imports": "from leetcode_py import TreeNode"`
- Use `TreeNode | None` for nullable tree parameters
- Test imports: Include TreeNode in test_imports
- Test setup: `root = TreeNode.from_list(root_list)`

### Linked List Problems

- Add `"solution_imports": "from leetcode_py import ListNode"`
- Use `ListNode | None` for nullable list parameters
- Test imports: Include ListNode in test_imports
- Test setup: `head = ListNode.from_list(head_list)`

### Design Problems

- Set `"solution_class_name"` to custom class name (e.g., "LRUCache")
- Multiple methods including `__init__`
- Complex test setup with operation sequences
- Import custom class in test_imports

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
