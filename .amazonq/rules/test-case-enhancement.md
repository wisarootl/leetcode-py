# Test Case Enhancement Rules

## Simple Enhancement Workflow

When user requests test case enhancement or **test reproducibility verification**:

### 1. Problem Resolution

- Use active file context or user-provided problem name
- If unclear, run: `poetry run python .templates/check_test_cases.py --threshold=10 --max=1`

### 2. Enhancement Process

```bash
# Simple 4-step process:
# 1. Update JSON template with more test cases (12-15 total)
# 2. Backup original
mv leetcode/{problem_name} .cache/leetcode/{problem_name}
# 3. Regenerate with enhanced tests
make p-gen PROBLEM={problem_name} FORCE=1 && make p-lint PROBLEM={problem_name}
# 4. Restore original solution, keep enhanced tests
cp .cache/leetcode/{problem_name}/solution.py leetcode/{problem_name}/solution.py
```

### 3. Verification

- Run `make p-test PROBLEM={problem_name}`
- Fix any incorrect expected values in test cases
- Update JSON template with corrections

### 4. Restore Backup

```bash
# Copy enhanced test_solution.py to backup
cp leetcode/{problem_name}/test_solution.py .cache/leetcode/{problem_name}/
# Restore all original files (preserves user edits)
rm -rf leetcode/{problem_name}
mv .cache/leetcode/{problem_name} leetcode/{problem_name}
```

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

```bash
# Find problems needing enhancement
poetry run python .templates/check_test_cases.py --threshold=10

# Test specific problem
make p-test PROBLEM={problem_name}

# Generate from JSON template
make p-gen PROBLEM={problem_name} FORCE=1

# Lint check
make p-lint PROBLEM={problem_name}
```

## Test Reproducibility Verification

Use this same workflow when CI tests fail due to reproducibility issues:

**Process Name**: Test Reproducibility Verification

**When to Use**:

- CI test failures in reproducibility checks
- Inconsistent test results between environments
- Missing edge cases causing coverage gaps
- Need to ensure 100% code coverage

## Success Criteria

- All tests pass with enhanced test cases
- Minimum 12 comprehensive test cases per problem
- Original solution code preserved
- **Enhanced test cases in final test_solution.py**
- JSON template updated for future regeneration
- **100% code coverage including edge cases**
