# Problem Creation Guide

## Quick Steps

1. Create JSON: `.templates/leetcode/json/{problem_name}.json`
2. Update Makefile: `PROBLEM ?= your_new_problem`
3. Generate: `make p-gen`
4. Verify: `make lint`
5. **If you edit generated files**: Update JSON template, then `make p-gen FORCE=1` to ensure reproducibility

## JSON Template Rules

- **Copy from reference examples** - don't create from scratch
- **Tree problems**: Use `.templates/leetcode/examples/tree.json5`
- **Basic problems**: Use `.templates/leetcode/examples/basic.json5`
- **Don't add extra fields** - templates are complete
- **Python naming convention**: Use snake_case for all parameter names (e.g., `new_interval` not `newInterval`)
- **If lint fails**: Fix JSON and regenerate, don't edit generated files
- **After any manual edits**: Always update JSON template and verify with `make p-gen FORCE=1`

## Tags (Optional)

```json
"tags": ["grind-75", "blind-75", "neetcode-150", "top-interview"]
```

## Helper Classes

- TreeNode: `from leetcode_py.tree_node import TreeNode`
- ListNode: `from leetcode_py.list_node import ListNode`
- New helpers: Add to `leetcode_py/`
