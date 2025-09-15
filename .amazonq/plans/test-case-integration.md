# Test Case Tool Organization Plan

## Decision: Cancel CLI Integration

After analysis, the test case checking functionality is a **development/maintenance tool** for repository maintainers, not end-user CLI functionality. Users of the `lcpy` CLI don't need to know about test case counts - they just want to generate and work with problems.

## New Plan: Move to Tools Directory

### 1. Move Script to Tools

```bash
# Move from .templates/ to leetcode_py/tools/
mv .templates/check_test_cases.py leetcode_py/tools/check_test_cases.py
```

### 2. Update Script Paths

Update the script to use correct paths for the new location:

- JSON templates: `leetcode_py/cli/resources/leetcode/json/problems/`
- Relative imports if needed

### 3. Add Makefile Target

Add convenient Makefile target for easy access:

```makefile
# Check test case coverage
check-test-cases:
	@echo "Checking test case coverage..."
	poetry run python leetcode_py/tools/check_test_cases.py --threshold=$(or $(THRESHOLD),10) --max=$(or $(MAX),10)
```

## Benefits of This Approach

- **Clear separation**: Development tools in `tools/`, user CLI in `cli/`
- **Easy access**: `make check-test-coverage` is simple and memorable
- **No CLI bloat**: Keeps `lcpy` focused on user needs
- **Maintainer friendly**: Still easy for repository maintainers to use
- **Consistent location**: Follows existing pattern with other tools in `leetcode_py/tools/`

## Usage After Migration

```bash
# Quick check for problems needing more test cases
make check-test-cases

# Check all problems (not just first 10)
make check-test-cases MAX=999

# Custom threshold and max
make check-test-cases THRESHOLD=12 MAX=5

# Direct usage (if needed)
poetry run python leetcode_py/tools/check_test_cases.py --threshold=12 --max=5
```

## Implementation Steps

1. **Move file**: `mv .templates/check_test_cases.py leetcode_py/tools/check_test_cases.py`
2. **Update paths**: Fix JSON template paths in the script
3. **Add Makefile target**: Add `check-test-cases` with THRESHOLD and MAX args
4. **Update documentation**: Update `.amazonq/rules/test-case-enhancement.md` to use new Makefile targets
5. **Test**: Verify the tool works from new location

## Success Criteria

- ✅ Script moved to `leetcode_py/tools/check_test_cases.py`
- ✅ Script works with correct JSON template paths
- ✅ `make check-test-cases` command works with args
- ✅ Documentation updated to reference new commands
- ✅ Tool remains fully functional for development use

This organization maintains clear separation between user-facing CLI tools and development/maintenance utilities.
