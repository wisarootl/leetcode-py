# Plan: Improve Cookiecutter Template for LeetCode Problems

## Overview

Improve the cookiecutter template to be more general and cover all LeetCode question types, including special cases like LRU Cache that use custom class names and multiple methods.

## Current Issues Identified

1. **Hard-coded class name**: Template assumes `Solution` class but some problems use custom classes (e.g., `LRUCache`)
2. **Single method assumption**: Template assumes one method but some problems have multiple methods (`__init__`, `get`, `put`)
3. **Complex test setup**: Current template doesn't handle operation-based testing for design problems
4. **Import handling**: Need better solution import structure
5. **Template parameter explosion**: Too many derived parameters that could be simplified

## Target Structure

```
.templates/leetcode/
├── {{cookiecutter.problem_name}}/
│   ├── __init__.py
│   ├── solution.py
│   ├── tests.py
│   ├── README.md
│   └── playground.ipynb
└── cookiecutter.json
```

## Phase 1: Analyze Problem Types

### 1.1 Universal Template Variables

- `solution_imports`: Required imports for solution.py (empty, TreeNode, ListNode, etc.)
- `test_imports`: All import lines for tests.py (pytest, loguru, TreeNode, test_utils, solution class)
- `solution_class_name`: Dynamic class name (Solution, LRUCache, etc.)
- `readme_description`: Problem description for README (supports HTML including images, preserves code snippets like `x`, `y`, `some_params`)
- `readme_examples`: Examples for README (supports HTML including images, typically uses code blocks for input/output)
- `readme_constraints`: Constraints for README
- `readme_additional`: Additional README sections
- `solution_methods`: List of methods with parameters/return types
- `test_methods`: List of test methods with parametrize and body
- `test_helper_methods`: List of test helper methods (setup_method, teardown_method, utility methods, etc.)

## Phase 2: Create New cookiecutter.json

### 2.1 Complete Template Variables Example

````json
{
    "problem_name": "two_sum",
    "solution_class_name": "Solution",
    "problem_number": "1",
    "problem_title": "Two Sum",
    "difficulty": "Easy",
    "topics": "Array, Hash Table",
    "tags": ["grind-75"],

    "readme_description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.\n\n<img src=\"example1.png\" alt=\"Array Example\" width=\"300\">\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.",
    "readme_examples": [
        {
            "content": "```\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\n```\n**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]."
        },
        {
            "content": "<img src=\"tree_example.png\" alt=\"Binary Tree\" width=\"200\">\n\n```\nInput: root = [4,2,7,1,3,6,9]\nOutput: [4,7,2,9,6,3,1]\n```\n**Explanation:** The tree is inverted as shown in the image above."
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

    "test_imports": "import pytest\nfrom loguru import logger\nfrom leetcode_py.test_utils import logged_test\nfrom .solution import Solution",
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

## Phase 3: Update Template Files

### 3.1 solution.py Template

```python
{{cookiecutter.solution_imports}}

class {{cookiecutter.solution_class_name}}:
    {% for method in cookiecutter.solution_methods %}
    # Time: O(?)
    # Space: O(?)
    def {{method.name}}(self, {{method.parameters}}) -> {{method.return_type}}:
        # TODO: Implement {{method.name}}
        return {{method.dummy_return}}

    {% endfor %}
```

### 3.2 tests.py Template

```python
{{cookiecutter.test_imports}}

class Test{{cookiecutter.solution_class_name}}:
    {% for method in cookiecutter.test_helper_methods %}
    def {{method.name}}(self{% if method.parameters %}, {{method.parameters}}{% endif %}):
        {{method.body}}

    {% endfor %}

    {% for method in cookiecutter.test_methods %}
    @pytest.mark.parametrize("{{method.parametrize}}", {{method.test_cases}})
    @logged_test
    def {{method.name}}(self, {{method.parametrize}}):
        {{method.body}}

    {% endfor %}
```

### 3.3 README.md Template

```markdown
# {{cookiecutter.problem_title}}

**Difficulty:** {{cookiecutter.difficulty}}
**Topics:** {{cookiecutter.topics}}
**Tags:** {{cookiecutter.tags | join(', ')}}
{% if cookiecutter.problem_number %}
**LeetCode:** [Problem {{cookiecutter.problem_number}}](https://leetcode.com/problems/{{cookiecutter.problem_name.replace('_', "-")}}/description/)
{% endif %}

## Problem Description

{{cookiecutter.readme_description}}

## Examples

{% for example in cookiecutter.readme_examples %}

### Example {{loop.index}}:

{{example.content}}
{% endfor %}

## Constraints

{{cookiecutter.readme_constraints}}

{% if cookiecutter.readme_additional %}
{{cookiecutter.readme_additional}}
{% endif %}
```

### 3.4 playground.ipynb Template

```json
{
    "cells": [
        {
            "cell_type": "code",
            "id": "imports",
            "source": ["{{cookiecutter.playground_imports}}"]
        },
        {
            "cell_type": "code",
            "id": "setup",
            "source": ["{{cookiecutter.playground_test_case}}"]
        },
        {
            "cell_type": "code",
            "id": "execute",
            "source": ["{{cookiecutter.playground_execution}}"]
        },
        {
            "cell_type": "code",
            "id": "test",
            "source": ["{{cookiecutter.playground_assertion}}"]
        }
    ]
}
```

## Phase 4: Simplify Parameter Generation

### 4.1 Reduce Template Complexity

- Remove derived parameters like `param_names`, `input_description`, etc.
- Generate these dynamically in the template using Jinja2 filters
- Focus on core data: methods, test_cases, problem metadata

### 4.2 Smart Defaults

- Auto-generate method names from problem names
- Auto-generate class names from problem names
- Default to "basic" problem type unless specified

## Phase 5: Testing & Validation

### 5.1 Test with Existing Problems

- Generate all current problems using new template
- Compare output with existing generated files
- Ensure no regression in functionality

### 5.2 Test Special Cases

- LRU Cache (design problem)
- Tree problems (TreeNode imports)
- Linked list problems (ListNode imports)
- Matrix problems (2D arrays)

## Phase 6: Integration

### 6.1 Update Generation Scripts

- Modify `gen.py` to work with new template structure
- Update Makefile commands
- Ensure backward compatibility with existing JSON files

### 6.2 Documentation

- Update problem creation guide
- Create examples for each problem type
- Document new template variables

## Success Criteria

1. ✅ Single cookiecutter template handles all problem types
2. ✅ Reduced template complexity (fewer derived parameters)
3. ✅ Support for design problems with multiple methods
4. ✅ Proper imports for tree/linked list problems
5. ✅ Clean, maintainable template structure
6. ✅ All existing problems can be regenerated without issues
7. ✅ New problem types can be easily added

## Implementation Order

1. Create new `cookiecutter.json` structure
2. Update template files with conditional logic
3. Test with basic problems (Two Sum)
4. Test with design problems (LRU Cache)
5. Test with tree/linked list problems
6. Validate all existing problems
7. Update generation scripts and documentation
