# Plan: Update CookieCutter Test Template to Use For Loop Instead of Parametrize

## Overview

Update the cookiecutter template for `test_solution.py` to use a for loop approach for test cases instead of the current `@pytest.mark.parametrize` decorator. This will make the test structure more explicit and easier to read.

## Current State Analysis

### Current Template Structure

- Uses `@pytest.mark.parametrize` decorator with `method.parametrize` and `method.test_cases`
- Test cases are stored as a single string in JSON: `"[([1, 2, 3], [1, 2, 3], True), ...]"`
- Generated test method signature includes all parameters: `(self, p_list: list[int | None], q_list: list[int | None], expected: bool)`

### Current JSON Structure

```json
"_test_methods": {
    "list": [
        {
            "name": "test_is_same_tree",
            "signature": "(self, p_list: list[int | None], q_list: list[int | None], expected: bool)",
            "parametrize": "p_list, q_list, expected",
            "test_cases": "[([1, 2, 3], [1, 2, 3], True), ([1, 2], [1, None, 2], False), ...]",
            "body": "result = run_is_same_tree(Solution, p_list, q_list)\nassert_is_same_tree(result, expected)"
        }
    ]
}
```

## Target State

### New Template Structure

- Keep `@pytest.mark.parametrize` decorator
- Use a for loop to iterate through individual test cases from the list
- Test method signature remains the same
- Only change: `test_cases` becomes a list instead of a string

### New JSON Structure

```json
"_test_methods": {
    "list": [
        {
            "name": "test_is_same_tree",
            "signature": "(self, p_list: list[int | None], q_list: list[int | None], expected: bool)",
            "parametrize": "p_list, q_list, expected",
            "test_cases": {
                "list": [
                    "([1, 2, 3], [1, 2, 3], True)",
                    "([1, 2], [1, None, 2], False)",
                    "([1, 2, 1], [1, 1, 2], False)"
                ]
            },
            "body": "result = run_is_same_tree(Solution, p_list, q_list)\nassert_is_same_tree(result, expected)"
        }
    ]
}
```

## Implementation Plan

### Phase 1: Update CookieCutter Template

1. **Update `test_solution.py` template**
    - Change from `{{method.test_cases}}` to `{{method.test_cases.list | join(', ')}}`
    - This follows the existing pattern used by other list fields in the template
    - Template line 30: `@pytest.mark.parametrize("{{method.parametrize}}", [{{method.test_cases.list | join(', ')}}])`
    - **✅ Validated:** Correctly follows existing "list" pattern used by `_tags`, `_readme_examples`, etc.

### Phase 2: Create JSON Migration Script

1. **Create `migrate_test_cases.py` script**
    - Parse existing JSON files in `leetcode_py/cli/resources/leetcode/json/problems/`
    - Convert `test_cases` string to `{"list": ["test_case1", "test_case2", ...]}` format
    - Keep all other fields exactly the same
    - Update only the `test_cases` field structure

### Phase 3: Update JSON Files

1. **Run migration script on all existing problem JSON files**
    - Process all 107 JSON files in the problems directory
    - Create backup of original files
    - Validate migrated JSON structure

### Phase 4: Testing and Validation

1. **Test generated templates**
    - Generate a test problem using updated template
    - Verify test cases run correctly with parametrize approach
    - Ensure JSON list format works with pytest parametrize

2. **Comprehensive validation with all problems**
    - Copy additional LeetCode problems to `.cache/leetcode` (if not already present)
    - Regenerate ALL problems from new design using updated template
    - Copy existing solutions from cache to regenerated problems
    - Run tests on all regenerated problems to ensure they still pass
    - Verify no regressions in test functionality
    - Document any issues found and fix them

### Phase 5: Update Documentation

1. **Update problem creation documentation**
    - Update `.cursor/commands/problem-creation.md` to reflect new JSON structure
    - Change `test_cases` format from string to `{"list": [...]}` in examples
    - Update template examples to show new format
    - Add note about migration for existing problems
2. **Update any other related documentation**
    - Check for other docs that reference `test_cases` format
    - Update examples in README or other guides if needed

## Benefits of New Approach

1. **Cleaner JSON Structure**: Test cases as `{"list": [...]}` object instead of single string
2. **Better Maintainability**: Easier to edit individual test cases in JSON files
3. **No Parsing Issues**: Avoids tuple conversion and complex JSON parsing
4. **Consistency**: Aligns with other JSON list fields in the structure
5. **Template Consistency**: Uses same pattern as other list fields (`| join(', ')`)

## Files to Modify

### Template Files

- `leetcode_py/cli/resources/leetcode/{{cookiecutter.problem_name}}/test_solution.py`

### Migration Script

- `migrate_test_cases.py` (new file)

### JSON Files

- All files in `leetcode_py/cli/resources/leetcode/json/problems/` (107 files)

### Generation Code

- **No changes needed** - The `test_cases` field is created manually, not by automated code
- The existing "list" pattern is already established and working correctly
- Phase 4 removed after investigation showed no automated generation code exists

## Implementation Steps

1. ✅ Create this plan document
2. ✅ Update cookiecutter template
3. ✅ Create migration script
4. ✅ Run migration on all JSON files
5. ✅ Test updated template generation
6. ✅ Validate all tests still work
7. 🔄 Update documentation (separate step - do not combine with implementation)

## Risk Mitigation

1. **Backup Strategy**: Create backups of all JSON files before migration
2. **Incremental Testing**: Test migration on a few files first
3. **Rollback Plan**: Keep original template and migration script for rollback
4. **Validation**: Ensure all existing tests still pass after migration

## Success Criteria

1. All existing JSON files successfully migrated to new list format
2. Generated test templates work with JSON array format for test_cases
3. All existing tests continue to pass with parametrize approach
4. JSON structure is cleaner and more maintainable
5. Template generation works correctly for new problems
6. **All regenerated problems pass their tests** (comprehensive validation)
7. No regressions in test functionality across the entire problem set
