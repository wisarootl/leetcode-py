# Create Template Example

Create single comprehensive example file with all template patterns.

## Goal

Replace multiple examples with one `example.json5` containing `valid_anagram` as base with rich comments for all variations.

## Structure

```
.templates/leetcode/examples/
└── example.json5      # Comprehensive template with all patterns
```

## Content Plan

Use `valid_anagram` as working example with comments showing all patterns.

## Reference Problems (5 total)

1. **`valid_anagram`** - Basic: string parameters, boolean return
2. **`invert_binary_tree`** - Tree: TreeNode imports/parameters
3. **`merge_two_sorted_lists`** - LinkedList: ListNode imports/parameters
4. **`lru_cache`** - Design: custom class, multiple methods, operations
5. **`implement_trie_prefix_tree`** - Trie: DictTree inheritance

## Implementation

**Prerequisites:** Complete these 5 problems first using `.amazonq/plans/migrate_problems_to_new_template.md`:

1. **`valid_anagram`** - Follow migration steps 1-8
2. **`invert_binary_tree`** - Follow migration steps 1-8
3. **`merge_two_sorted_lists`** - Follow migration steps 1-8
4. **`lru_cache`** - Follow migration steps 1-8
5. **`implement_trie_prefix_tree`** - Follow migration steps 1-8

**Then create example:**

1. Create `.templates/leetcode/examples/example.json5`
2. Use `valid_anagram` as base structure
3. Add comprehensive comments showing variations from the other 4 problems
4. Test generation works with the example

## Key Sections

- Problem identification (basic vs design class names)
- Imports (empty, TreeNode, ListNode, DictTree)
- Methods (single vs multiple, **init** patterns)
- Tests (simple vs operations-based)
- Playground (single quotes for strings)
