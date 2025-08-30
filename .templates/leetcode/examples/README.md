# LeetCode Template Examples

Reference templates for creating new LeetCode problems. **Copy from these examples** - don't create from scratch.

## Usage

1. **Choose the right template** based on problem type
2. **Copy the entire structure** to `.templates/leetcode/json/{problem_name}.json`
3. **Update all fields** with your problem's data
4. **Generate**: `make p-gen PROBLEM=your_problem`

## Templates

### `basic.json5`

- **Use for**: Array, string, number, hash table problems
- **Examples**: Two Sum, Valid Anagram, Contains Duplicate
- **Features**: Simple parameters, direct assertions

### `tree.json5`

- **Use for**: Binary tree problems
- **Examples**: Invert Binary Tree, Maximum Depth, Same Tree
- **Features**: TreeNode import, array-to-tree conversion, tree logging

### `linked_list.json5`

- **Use for**: Linked list problems
- **Examples**: Reverse Linked List, Merge Two Lists, Cycle Detection
- **Features**: ListNode import, array-to-list conversion, list logging

### `string.json5`

- **Use for**: String manipulation problems
- **Examples**: Valid Palindrome, Longest Substring, Anagrams
- **Features**: String parameters, boolean/string returns

### `matrix.json5`

- **Use for**: 2D array/matrix problems
- **Examples**: Rotate Image, Spiral Matrix, Set Matrix Zeroes
- **Features**: Matrix parameters, in-place operation testing

## Key Fields

### Required Core Fields

- `problem_name`, `class_name`, `method_name`
- `problem_number`, `problem_title`, `difficulty`, `topics`
- `problem_description`, `examples`, `constraints`
- `parameters`, `return_type`, `dummy_return`

### Test Configuration

- `test_cases`: Array of `{args, expected}` objects
- `param_names`: Parameter names for test methods
- `test_setup`: Code to convert test data (e.g., arrays to TreeNode)
- `assertion_code`: How to compare result with expected

### Notebook Setup

- `test_input_setup`: Code for notebook input cell
- `expected_output_setup`: Code for notebook expected cell
- `imports`: Required imports (TreeNode, ListNode, etc.)

## Rules

1. **Copy structure exactly** - all fields are required
2. **Use modern Python syntax**: `list[int]`, `TreeNode | None`
3. **Match existing patterns** - see current JSON files for reference
4. **Test thoroughly** - run `make lint` and `make p-test` after generation
