# LeetCode Problem Template Examples

This directory contains comprehensive JSON5 template examples for different types of LeetCode problems. These examples serve as references when creating new problems using the universal cookiecutter template.

## Template Types

### 1. `basic.json5` - Basic Algorithm Problems

**Use for:** Array, string, number, hash table problems
**Examples:** Container With Most Water, Two Sum, Valid Palindrome
**Key features:**

- Simple `Solution` class with single method
- Standard test parametrization
- Basic playground setup

### 2. `tree.json5` - Binary Tree Problems

**Use for:** Binary tree, BST, tree traversal problems
**Examples:** Invert Binary Tree, Maximum Depth, Serialize Tree
**Key features:**

- `TreeNode` imports and conversions
- `TreeNode.from_list()` and `TreeNode.to_list()` in tests
- Tree visualization support

### 3. `linked_list.json5` - Linked List Problems

**Use for:** Singly/doubly linked list problems
**Examples:** Reverse Linked List, Merge Lists, Detect Cycle
**Key features:**

- `ListNode` imports and conversions
- `ListNode.from_list()` and `ListNode.to_list()` in tests
- Arrow visualization support

### 4. `design.json5` - Data Structure Design Problems

**Use for:** Design problems requiring custom classes
**Examples:** LRU Cache, Implement Trie, Design HashMap
**Key features:**

- Custom class names (not `Solution`)
- Multiple methods including `__init__`
- Complex operation sequence testing
- Type annotations for complex test logic

### 5. `matrix.json5` - 2D Array/Matrix Problems

**Use for:** Matrix manipulation, 2D array problems
**Examples:** Spiral Matrix, Rotate Image, Search 2D Matrix
**Key features:**

- 2D array type annotations (`list[list[int]]`)
- Visual examples with images
- Matrix-specific test cases

## Usage Guidelines

### Problem Type Detection

1. **Basic**: Single algorithm, simple input/output
2. **Tree**: Mentions "tree", "node", uses tree terminology
3. **Linked List**: Mentions "linked list", "node", list operations
4. **Design**: "Design", "Implement", multiple operations
5. **Matrix**: "matrix", "2D array", "grid", visual layout

### Key Template Fields

#### Required Fields

- `problem_name`: snake_case identifier
- `solution_class_name`: "Solution" or custom class name
- `problem_number`: LeetCode number as string
- `problem_title`: Exact LeetCode title
- `difficulty`: "Easy", "Medium", or "Hard"
- `topics`: Comma-separated topic string
- `solution_methods`: Array of method definitions

#### Important Patterns

- **Type Hints**: Use modern syntax (`list[int]`, `dict[str, int]`, `Type | None`)
- **Method Names**: Always snake_case
- **Test Cases**: String representation of Python data structures
- **Imports**: Include necessary helper classes (TreeNode, ListNode)

#### PascalCase Naming Rules

For `solution_class_name` and `test_class_name` properties:

- **Acronyms**: Keep all caps ("LRUCache" not "LruCache")
- **Roman numerals**: Keep all caps ("ReverseLinkedListII" not "ReverseLinkedListIi")
- **Common patterns**: "BST", "DFS", "BFS", "API", "URL", "HTML", "JSON", "XML"

### Template Selection Process

1. Identify problem type from description/title
2. Choose appropriate template from examples
3. Customize fields for specific problem
4. Ensure imports match problem requirements
5. Verify test setup matches data structures used

## Validation

All templates are validated against:

- Cookiecutter template compatibility
- Linting requirements (black, isort, ruff, mypy)
- Test framework integration
- Notebook JSON format compliance

## Notes

- JSON5 format allows comments for documentation
- All examples are based on working, tested templates
- Templates are designed for the universal cookiecutter system
- Examples include both simple and complex problem patterns
