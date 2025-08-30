# LeetCode Problem Template Examples

These JSON5 files serve as reference templates for creating new LeetCode problems. Each template is designed to help LLMs parse raw problem text from leetcode.com into the correct JSON format.

## Template Types

### 1. `basic.json5` - Array/Number Problems

- **Use for**: Array manipulation, hash table, basic algorithms
- **Examples**: Two Sum, Contains Duplicate, Product of Array Except Self
- **Key features**: Simple parameters, basic return types, no special imports

### 2. `tree.json5` - Binary Tree Problems

- **Use for**: Binary tree traversal, tree manipulation, tree construction
- **Examples**: Invert Binary Tree, Maximum Depth, Validate BST
- **Key features**: TreeNode import, array-to-tree conversion, tree-specific logging

### 3. `linked_list.json5` - Linked List Problems

- **Use for**: Singly linked list manipulation, list reversal, merging
- **Examples**: Reverse Linked List, Merge Two Lists, Remove Nth Node
- **Key features**: ListNode import, array-to-list conversion, multiple parameters

### 4. `string.json5` - String Problems

- **Use for**: String manipulation, validation, parsing
- **Examples**: Valid Parentheses, Longest Substring, Palindrome Check
- **Key features**: String parameters, boolean returns, validation patterns

### 5. `matrix.json5` - 2D Array/Matrix Problems

- **Use for**: Matrix operations, 2D array manipulation, grid problems
- **Examples**: Rotate Image, Spiral Matrix, Set Matrix Zeroes
- **Key features**: 2D list types, in-place modifications, deep copy for testing

## Usage Instructions

1. **Choose the appropriate template** based on the problem's primary data structure
2. **Copy the template structure** and fill in the specific problem details
3. **Follow the comments** for guidance on each field
4. **Use modern Python syntax** (e.g., `list[int]` instead of `List[int]`)
5. **Test the generated JSON** with `make q-gen QUESTION=your_problem`

## Key Conventions

- **Naming**: Use snake_case for `question_name` and `method_name`, PascalCase for `class_name`
- **Types**: Use modern Python type hints (`list[int]`, `TreeNode | None`)
- **Parameters**: Match the exact parameter names from the LeetCode method signature
- **Test Cases**: Use the same data format as the examples (arrays for trees/lists)
- **Imports**: Only include necessary imports (`TreeNode`, `ListNode`, etc.)

## Common Patterns

### Return Types & Dummy Returns

- `bool` → `"False"`
- `int` → `"0"`
- `str` → `"\"\""`
- `list[int]` → `"[]"`
- `TreeNode | None` → `"None"`
- `ListNode | None` → `"None"`

### Test Parameter Naming

- **Basic problems**: `param1, param2, expected`
- **Tree problems**: `root_list, expected_list` (converts arrays to TreeNode)
- **Linked List problems**: `head_list, param2, expected_list` (converts arrays to ListNode)

### Test Setup Patterns

- **Basic**: No setup needed (`""`)
- **Tree**: `"root = TreeNode.from_list(root_list)\\nexpected = TreeNode.from_list(expected_list)"`
- **Linked List**: `"head = ListNode.from_list(head_list)\\nexpected = ListNode.from_list(expected_list)"`
- **Matrix (in-place)**: `"import copy\\noriginal_matrix = copy.deepcopy(matrix)"`

These templates ensure consistency and proper integration with the existing test framework and validation system.
