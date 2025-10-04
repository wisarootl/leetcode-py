# Test Quality Assurance Rules

## CRITICAL: Follow These Steps EXACTLY - No Deviations

### 1. Problem Resolution

- Use active file context or user-provided problem name
- If unclear, run: `poetry run python -m leetcode_py.tools.check_test_cases --threshold=10 --max=1`

### 2. Test Reproducibility Verification Process

**MANDATORY 6-Step Process - Execute in Order:**

```bash
# Step 1: Backup original files
cp -r leetcode/{problem_name} leetcode/{problem_name}_backup

# Step 2: Regenerate from JSON template (use Makefile, NOT poetry run)
make p-gen PROBLEM={problem_name} FORCE=1

# Step 3: Restore original solution ONLY
cp leetcode/{problem_name}_backup/solution.py leetcode/{problem_name}/solution.py

# Step 4: Verify linting pass (CRITICAL for CI)
make p-lint PROBLEM={problem_name}

# Step 5: Verify tests pass (expected to fail if solution is incomplete)
make p-test PROBLEM={problem_name}

# Step 6: Cleanup
rm -rf leetcode/{problem_name}_backup
```

### 3. What NOT to Do

- ❌ **NEVER edit cookiecutter templates** (`{{cookiecutter.problem_name}}/` files)
- ❌ **NEVER use `poetry run python -m leetcode_py.cli.main gen`** - use `make p-gen` instead
- ❌ **NEVER modify helpers.py manually** - let regeneration handle it
- ❌ **NEVER skip mypy verification** - this is the main CI issue
- ❌ **NEVER assume tests will pass** - they may fail if solution is incomplete

### 4. What to Do

- ✅ **ALWAYS use `make p-gen PROBLEM={problem_name} FORCE=1`** for regeneration
- ✅ **ALWAYS verify mypy passes** before considering task complete
- ✅ **ALWAYS restore original solution** after regeneration
- ✅ **ALWAYS check JSON template** if mypy fails (look for `assert_assert_` bugs)

## Test Case Standards

### Coverage Requirements

- **Minimum 12 test cases** per problem
- **Edge cases**: Empty inputs, single elements, boundary values
- **Corner cases**: Maximum/minimum constraints, duplicates, sorted arrays
- **Normal cases**: Mixed scenarios with varied complexity

### JSON Format

- Use single quotes for Python strings: `'hello'` not `"hello"`
- Follow existing parametrize format
- Ensure valid Python list syntax in test_cases field

## Quick Commands

### CLI Commands (Recommended)

```bash
# Generate enhanced problem
poetry run lcpy gen -s {problem_name} -o leetcode --force

# Test specific problem
make p-test PROBLEM={problem_name}

# Lint check
make p-lint PROBLEM={problem_name}
```

### Development Commands

```bash
# Find problems needing enhancement
poetry run python -m leetcode_py.tools.check_test_cases --threshold=10

# Check all problems (no limit)
poetry run python -m leetcode_py.tools.check_test_cases --threshold=10 --max=none

# Check with custom threshold
poetry run python -m leetcode_py.tools.check_test_cases --threshold=12

# Generate from JSON template (uses poetry run lcpy internally)
make p-gen PROBLEM={problem_name} FORCE=1
```

## Common Issues & Solutions

### Issue: `assert_assert_missing_number` Error

**Cause**: JSON template has `helpers_assert_name: "assert_missing_number"` but template adds `assert_` prefix
**Solution**: Change JSON to `helpers_assert_name: "missing_number"` so template generates `assert_missing_number`

### Issue: mypy Import Errors

**Cause**: Regenerated helpers.py doesn't match test imports
**Solution**: Use `make p-gen` (not poetry run) and verify JSON template is correct

### Issue: Tests Fail After Regeneration

**Expected**: Tests may fail if solution is incomplete (returns 0 or placeholder)
**Action**: This is normal - focus on mypy passing, not test results

## Success Criteria

- ✅ **mypy passes** with no errors (CRITICAL for CI)
- ✅ **Test structure matches JSON template** exactly
- ✅ **Original solution preserved** (user's code intact)
- ✅ **helpers.py generated correctly** (no `assert_assert_` bugs)
- ✅ **Reproducibility verified** (can regenerate consistently)

## When to Use This Workflow

- GitHub Actions CI failures due to mypy errors
- Test reproducibility verification requests
- Need to ensure test structure matches JSON template
- CI test failures in reproducibility checks
