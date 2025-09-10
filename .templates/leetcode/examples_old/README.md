# JSON Template Examples

This directory contains comprehensive examples for creating LeetCode problem templates.

## Files

- **`basic.json5`** - Covers all standard problem types:
    - Array problems (Container With Most Water)
    - String problems (with JSON escaping notes)
    - Tree problems (import and parameter examples)
    - Linked list problems (import and parameter examples)
    - Matrix problems
    - Number problems

- **`design.json5`** - Data structure design problems:
    - Custom class names (LRUCache, not Solution)
    - Multiple methods including `__init__`
    - Complex test setup with operation sequences
    - Custom imports

## Key Differences

### Standard Problems (basic.json5)

- `solution_class_name`: Always "Solution"
- Single method (usually)
- Simple test cases with direct assertions
- Standard imports

### Design Problems (design.json5)

- `solution_class_name`: Custom class name (e.g., "LRUCache")
- Multiple methods including constructor
- Operation sequence testing
- Import custom class in tests

## Critical Notes

- **JSON Escaping**: Use single quotes for Python strings in playground fields
- **Type Hints**: Use modern syntax (`list[int]`, `TreeNode | None`)
- **PascalCase**: Keep acronyms ALL CAPS (LRUCache, ReverseLinkedListII)
