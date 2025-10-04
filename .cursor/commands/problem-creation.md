# Problem Creation Guide

## Assistant Workflow

When user requests a problem by **number** or **name/slug**, the assistant will:

1. **Scrape** problem data using `poetry run lcpy scrape`
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

**If user does not specify a problem number or name/slug**, run:

```bash
poetry run python .cursor/.dev/next_problem.py
```

This will suggest the next problem to work on from the available problem lists based on completion status.

## Scraping Commands

```bash
# Fetch by number
poetry run lcpy scrape -n 1

# Fetch by slug
poetry run lcpy scrape -s "two-sum"
```

## JSON Template Format

Required fields for `leetcode_py/cli/resources/leetcode/json/problems/{problem_name}.json`:

**CRITICAL: Use single quotes for Python strings in playground fields to avoid JSON escaping issues with Jupyter notebooks.**

**JSON Escaping Rules:**

- `playground_test_case`: Use single quotes for string literals (e.g., `s = 'hello'` not `s = "hello"`)
- `playground_execution`: Use single quotes for string literals
- `playground_assertion`: Use single quotes for string literals
- Double quotes in JSON + cookiecutter + Jupyter notebook = triple escaping issues

**Test Cases Format:**

- `test_cases`: Use structured format with `{"list": ["..."]}` instead of string arrays
- Each test case should be a string representation of the tuple/parameters
- Example: `{"list": ["('input1', 'input2', expected)", "('input3', 'input4', expected)"]}`

**IMPORTANT: Create actual JSON files, not JSON5**

The template below uses JSON5 format with comments for documentation purposes only. When creating the actual `.json` file, you must:

1. **Remove all comments** (lines starting with `//`)
2. **Use proper JSON syntax** with quoted property names
3. **Save as `.json` file** (not `.json5`)

**Template with comments (JSON5 format for reference only):**

````json5
{
    // ============================================================================
    // COMPREHENSIVE LEETCODE TEMPLATE EXAMPLE
    // ============================================================================
    // This example demonstrates ALL template patterns using valid_anagram as base
    // with comprehensive comments showing variations for different problem types.
    //
    // REFERENCE PROBLEMS (see .templates/leetcode/json/ for complete examples):
    // 1. valid_anagram        - Basic: string parameters, boolean return
    // 2. invert_binary_tree   - Tree: TreeNode imports/parameters
    // 3. merge_two_sorted_lists - LinkedList: ListNode imports/parameters
    // 4. lru_cache           - Design: custom class, multiple methods, operations
    // 5. implement_trie_prefix_tree - Trie: DictTree inheritance
    // ============================================================================

    // === PROBLEM IDENTIFICATION ===
    problem_name: "valid_anagram", // snake_case: used for directory/file names
    solution_class_name: "Solution", // "Solution" for basic problems
    // "LRUCache" for design problems
    // "Trie(DictTree[str])" for inheritance
    problem_number: "242", // LeetCode problem number as string
    problem_title: "Valid Anagram", // Exact title from LeetCode
    difficulty: "Easy", // Easy, Medium, Hard
    topics: "Hash Table, String, Sorting", // Comma-separated topics from LeetCode
    _tags: { list: ["grind-75"] }, // Optional: common problem set tags
    // Use _tags wrapper for cookiecutter lists

    // === README CONTENT ===
    // IMPORTANT: Preserve rich HTML content from LeetCode including:
    // - Code snippets with backticks: `code`
    // - Bold text: **bold** or <strong>bold</strong>
    // - Italic text: *italic* or <em>italic</em>
    // - Images: ![Example](https://assets.leetcode.com/uploads/...)
    // - HTML formatting: <p>, <br>, <ul>, <li>, etc.
    // - Mathematical expressions and special characters
    readme_description: "Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.",

    _readme_examples: {
        // Use _readme_examples wrapper for cookiecutter lists
        list: [
            { content: '```\nInput: s = "anagram", t = "nagaram"\nOutput: true\n```' },
            { content: '```\nInput: s = "rat", t = "car"\nOutput: false\n```' },
            // For tree problems: Include images
            // { "content": "![Example 1](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)\n\n```\nInput: root = [4,2,7,1,3,6,9]\nOutput: [4,7,2,9,6,3,1]\n```" }
        ],
    },

    readme_constraints: "- 1 <= s.length, t.length <= 5 * 10^4\n- s and t consist of lowercase English letters.",
    readme_additional: "**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?",

    // === HELPER FUNCTIONS ===
    // New template system uses helper functions for cleaner test organization
    helpers_imports: "", // Empty for basic problems
    // "from leetcode_py import TreeNode" for tree problems
    // "from leetcode_py import ListNode" for linked list problems
    helpers_content: "", // Additional helper content if needed
    helpers_run_name: "is_anagram", // Function name matching main method
    helpers_run_signature: "(solution_class: type, s: str, t: str)",
    // For tree: "(solution_class: type, root_list: list[int | None])"
    // For linked list: "(solution_class: type, list1_vals: list[int], list2_vals: list[int])"
    // For design: "(solution_class: type, operations: list[str], inputs: list[list[int]])"
    helpers_run_body: "    implementation = solution_class()\n    return implementation.is_anagram(s, t)",
    // For tree: "    root = TreeNode[int].from_list(root_list)\n    implementation = solution_class()\n    return implementation.invert_tree(root)"
    // For design: "    cache = None\n    results: list[int | None] = []\n    # ... operation loop ...\n    return results, cache"
    helpers_assert_name: "is_anagram", // Function name matching main method
    helpers_assert_signature: "(result: bool, expected: bool) -> bool",
    // For tree: "(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool"
    // For design: "(result: list[int | None], expected: list[int | None]) -> bool"
    helpers_assert_body: "    assert result == expected\n    return True",
    // For tree: "    expected = TreeNode[int].from_list(expected_list)\n    assert result == expected\n    return True"

    // === SOLUTION TEMPLATE ===
    solution_imports: "", // Empty for basic problems
    // "from leetcode_py import TreeNode" for tree problems
    // "from leetcode_py import ListNode" for linked list problems
    // "from leetcode_py.data_structures import DictTree, RecursiveDict" for trie problems
    solution_contents: "", // Additional content before class definition
    solution_class_content: "", // Content inside class definition (usually empty)

    // === TEST CONFIGURATION ===
    test_imports: "import pytest\nfrom leetcode_py import logged_test\nfrom .helpers import assert_is_anagram, run_is_anagram\nfrom .solution import Solution",
    // For design: "from .solution import LRUCache" instead of Solution
    test_content: "", // Additional test content
    test_class_name: "ValidAnagram", // PascalCase: TestClassName for pytest class
    test_class_content: "    def setup_method(self):\n        self.solution = Solution()",
    // Empty for design problems: ""

    // === SOLUTION METHODS ===
    _solution_methods: {
        // Use _solution_methods wrapper for cookiecutter lists
        list: [
            {
                name: "is_anagram", // snake_case method name
                signature: "(self, s: str, t: str) -> bool", // Full method signature with type hints
                // For tree: "(self, root: TreeNode[int] | None) -> TreeNode[int] | None"
                // For linked list: "(self, list1: ListNode[int] | None, list2: ListNode[int] | None) -> ListNode[int] | None"
                body: "        # TODO: Implement is_anagram\n        return False",
                // For design problems with __init__:
                // { "name": "__init__", "signature": "(self, capacity: int) -> None", "body": "        # TODO: Initialize\n        pass" }
            },
        ],
    },

    // === TEST HELPER METHODS ===
    _test_helper_methods: {
        // Use _test_helper_methods wrapper for cookiecutter lists
        list: [
            { name: "setup_method", parameters: "", body: "self.solution = Solution()" },
            // Empty list for design problems: []
        ],
    },

    // === TEST METHODS ===
    _test_methods: {
        // Use _test_methods wrapper for cookiecutter lists
        list: [
            {
                name: "test_is_anagram", // test_{method_name}
                signature: "(self, s: str, t: str, expected: bool)", // Method signature with type hints
                parametrize: "s, t, expected", // pytest parametrize parameters
                // For tree: "root_list, expected_list"
                // For design: "operations, inputs, expected"
                test_cases: {
                    list: [
                        "('anagram', 'nagaram', True)",
                        "('rat', 'car', False)",
                        "('listen', 'silent', True)",
                        "('hello', 'bello', False)",
                        "('', '', True)",
                        "('a', 'a', True)",
                        "('a', 'b', False)",
                        "('ab', 'ba', True)",
                        "('abc', 'bca', True)",
                        "('abc', 'def', False)",
                        "('aab', 'abb', False)",
                        "('aabbcc', 'abcabc', True)",
                        "('abcd', 'abcde', False)",
                        "('race', 'care', True)",
                        "('elbow', 'below', True)",
                        "('study', 'dusty', True)",
                        "('night', 'thing', True)",
                        "('stressed', 'desserts', True)",
                    ],
                },
                // For tree: {"list": ["([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])", "([2, 1, 3], [2, 3, 1])", "([], [])"]}
                // For design: {"list": ["(['LRUCache', 'put', 'get'], [[2], [1, 1], [1]], [None, None, 1])"]}
                body: "        result = run_is_anagram(Solution, s, t)\n        assert_is_anagram(result, expected)",
                // For tree: "        result = run_invert_tree(Solution, root_list)\n        assert_invert_tree(result, expected_list)"
                // For design: "        result, _ = run_lru_cache(LRUCache, operations, inputs)\n        assert_lru_cache(result, expected)"
            },
        ],
    },

    // === PLAYGROUND NOTEBOOK ===
    // CRITICAL: Use single quotes for Python strings to avoid JSON escaping issues with Jupyter notebooks
    // Double quotes in JSON + cookiecutter + Jupyter notebook = triple escaping issues
    // ALWAYS use single quotes: s = 'hello', not s = "hello"
    playground_imports: "from helpers import run_is_anagram, assert_is_anagram\nfrom solution import Solution",
    // For tree: "from helpers import run_invert_tree, assert_invert_tree\nfrom solution import Solution\nfrom leetcode_py import TreeNode"
    // For design: "from helpers import run_lru_cache, assert_lru_cache\nfrom solution import LRUCache"
    playground_setup: "# Example test case\ns = 'anagram'\nt = 'nagaram'\nexpected = True",
    // For tree: "# Example test case\nroot_list: list[int | None] = [4, 2, 7, 1, 3, 6, 9]\nexpected_list: list[int | None] = [4, 7, 2, 9, 6, 3, 1]"
    // For design: "# Example test case\noperations = ['LRUCache', 'put', 'get']\ninputs = [[2], [1, 1], [1]]\nexpected = [None, None, 1]"
    playground_run: "result = run_is_anagram(Solution, s, t)\nresult",
    // For tree: "result = run_invert_tree(Solution, root_list)\nresult"
    // For design: "result, cache = run_lru_cache(LRUCache, operations, inputs)\nprint(result)\ncache"
    playground_assert: "assert_is_anagram(result, expected)",
    // For tree: "assert_invert_tree(result, expected_list)"
    // For design: "assert_lru_cache(result, expected)"

    // ============================================================================
    // PROBLEM TYPE VARIATIONS SUMMARY:
    // ============================================================================
    //
    // BASIC PROBLEMS (valid_anagram):
    // - solution_class_name: "Solution"
    // - solution_imports: ""
    // - Simple method signatures: "(self, s: str, t: str) -> bool"
    // - Basic test cases: structured format with {"list": ["..."]}
    // - Playground: single quotes for strings
    //
    // TREE PROBLEMS (invert_binary_tree):
    // - solution_class_name: "Solution"
    // - solution_imports: "from leetcode_py import TreeNode"
    // - Tree method signatures: "(self, root: TreeNode[int] | None) -> TreeNode[int] | None"
    // - Helper functions use TreeNode.from_list()
    // - Test cases: structured format with list representations of trees
    // - Playground: TreeNode imports and list conversions
    //
    // LINKED LIST PROBLEMS (merge_two_sorted_lists):
    // - solution_class_name: "Solution"
    // - solution_imports: "from leetcode_py import ListNode"
    // - List method signatures: "(self, list1: ListNode[int] | None, list2: ListNode[int] | None) -> ListNode[int] | None"
    // - Helper functions use ListNode.from_list()
    // - Test cases: structured format with list representations of linked lists
    // - Playground: ListNode imports and list conversions
    //
    // DESIGN PROBLEMS (lru_cache):
    // - solution_class_name: "LRUCache" (custom class name)
    // - Multiple methods including __init__
    // - Operations-based testing: structured format with operations, inputs, expected arrays
    // - Complex test body with operation loops
    // - Helper functions return (results, instance) for debugging
    // - Playground: print results, return instance
    // - test_class_content: "" (no setup_method)
    //
    // INHERITANCE PROBLEMS (implement_trie_prefix_tree):
    // - solution_class_name: "Trie(DictTree[str])" (with inheritance)
    // - solution_imports: "from leetcode_py.data_structures import DictTree, RecursiveDict"
    // - Custom class with inheritance from DictTree
    // - Operations-based testing with structured format like design problems
    // - Helper functions return (results, instance) for debugging
    //
    // MULTIPLE SOLUTIONS (invert_binary_tree, lru_cache):
    // - Add parametrize for solution classes in test files:
    //   @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    //   @pytest.mark.parametrize("solution_class", [LRUCache, LRUCacheWithDoublyList])
    // - Update test method signature to include solution_class parameter
    // - Import all solution classes in test file
    // ============================================================================
}
````

**IMPORTANT: When creating the actual .json file, convert the above JSON5 to valid JSON by:**

1. **Remove all comments** (lines starting with `//`)
2. **Keep all quoted property names** (already done above)
3. **Save as `.json` file** (not `.json5`)

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

Common tags: `["grind-75", "grind", "blind-75", "neetcode-150", "algo-master-75"]`
