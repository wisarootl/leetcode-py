# Problem Creation Guide

## Assistant Workflow

When user requests a problem by **number** or **name/slug**, the assistant will:

1. **Scrape** problem data using `lcpy scrape`
2. **Transform** data into proper JSON template format
3. **CRITICAL: Include images** - Extract image URLs from scraped data and add to readme_examples with format: `![Example N](image_url)\n\n` before code blocks
    - Check scraped data for image URLs in the `raw_content` field
    - Look for patterns: `https://assets.leetcode.com/uploads/...` or `<img alt="" src="..." />`
    - Common patterns: `kthtree1.jpg`, `kthtree2.jpg`, `clone_graph.png`, `container.jpg`
    - Images provide crucial visual context, especially for tree and graph problems
    - Always verify images are included in `readme_examples` and accessible
4. **Create** JSON file in `leetcode_py/cli/resources/leetcode/json/problems/{problem_name}.json`
5. **Update tags.json5** - If user specifies tags, manually add problem name to corresponding tag arrays in `leetcode_py/cli/resources/leetcode/json/tags.json5`
6. **Update** Makefile with `PROBLEM ?= {problem_name}`
7. **Generate** problem structure using `make p-gen`
8. **Verify** with `make p-lint` - fix template issues in JSON if possible, or manually fix generated files if template limitations
9. **Iterate** if JSON fixes: re-run `make p-gen PROBLEM={problem_name} FORCE=1` and `make p-lint` until passes to ensure reproducibility

## Scraping Commands

```bash
# Fetch by number
lcpy scrape -n 1

# Fetch by slug
lcpy scrape -s "two-sum"
```

## JSON Template Format

Required fields for `leetcode_py/cli/resources/leetcode/json/problems/{problem_name}.json`:

**CRITICAL: Use single quotes for Python strings in playground fields to avoid JSON escaping issues with Jupyter notebooks.**

**JSON Escaping Rules:**

- `playground_test_case`: Use single quotes for string literals (e.g., `s = 'hello'` not `s = "hello"`)
- `playground_execution`: Use single quotes for string literals
- `playground_assertion`: Use single quotes for string literals
- Double quotes in JSON + cookiecutter + Jupyter notebook = triple escaping issues

**Reference the complete template example:**

See `leetcode_py/cli/resources/leetcode/examples/example.json5` for a comprehensive template with:

- All field definitions and variations
- Comments explaining each field
- Examples for different problem types (basic, tree, linked list, design, trie)
- Proper JSON escaping rules for playground fields
- Multiple solution class patterns

## Naming Conventions

- **problem_name**: snake_case (e.g., "two_sum", "valid_palindrome")
- **solution_class_name**: Usually "Solution", except for design problems (e.g., "LRUCache")
- **test_class_name**: PascalCase (e.g., "TwoSum", "ValidPalindrome")
- **method_name**: snake_case (e.g., "two_sum", "is_palindrome")
- **parameters**: Use snake_case for all parameter names

### PascalCase Rules for Properties

When creating JSON properties that use PascalCase (solution_class_name, test_class_name):

- **Acronyms**: Keep all caps (e.g., "LRUCache" not "LruCache")
- **Roman numerals**: Keep all caps (e.g., "ReverseLinkedListII" not "ReverseLinkedListIi")
- **Common patterns**: "BST", "DFS", "BFS", "API", "URL", "HTML", "JSON", "XML"

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
- **NEVER include custom solution classes** in test_imports - only import the main solution class specified in solution_class_name

### Dict-based Tree Problems (Trie, etc.)

- Add `"solution_imports": "from leetcode_py.data_structures import DictTree"`
- Inherit from `DictTree[str]` for string-based trees like Trie
- Provides automatic visualization capabilities
- Use `dict[str, Any]` for internal tree structure

## Generation Commands

```bash
# Generate problem
make p-gen PROBLEM={problem_name}

# Force regenerate (if files exist)
make p-gen PROBLEM={problem_name} FORCE=1

# Test specific problem
make p-test PROBLEM={problem_name}

# Lint problem only (faster)
make p-lint PROBLEM={problem_name}

# Lint entire project
make lint
```

## Tags (Optional)

Common tags: `["grind-75", "blind-75", "neetcode-150", "top-interview"]`
