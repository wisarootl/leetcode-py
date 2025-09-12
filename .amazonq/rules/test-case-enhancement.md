# Test Case Enhancement Rules

## Assistant Workflow for Adding Comprehensive Test Cases

When user requests to enhance test cases for a problem, the assistant will:

### 1. Problem Resolution (Priority Order)

- **FIRST**: Try to resolve from context - check active file path or user-provided problem name
- **SECOND**: If context resolution fails, THEN run `poetry run python .templates/check_test_cases.py --threshold=10 --max=1` to auto-detect 1 problem with <10 test cases
- **LAST**: If both above fail, ask user to explicitly specify problem name

### 2. Test Case Generation

- Read `leetcode/{problem_name}/README.md` for problem understanding
- Analyze existing test cases in `leetcode/{problem_name}/tests.py`
- Generate comprehensive test cases covering:
    - **Edge cases**: Empty inputs, single elements, boundary values
    - **Corner cases**: Maximum/minimum constraints, special patterns
    - **Normal cases**: Typical scenarios with varied complexity
    - **Error cases**: Invalid inputs (if applicable)

### 3. Initial Validation

- Run `make p-test PROBLEM={problem_name}` to verify current implementation
- **If errors found**:
    - DO NOT update implementation automatically
    - Only update test cases if they're incorrect
    - If implementation seems wrong, ASK USER first before modifying

### 4. JSON Template Update

- Update corresponding `.templates/leetcode/json/{problem_name}.json`
- Add new test cases to `test_cases` field in proper format
- Maintain existing test structure and naming conventions

### 5. Backup and Regeneration Process

- **Backup**: Move `leetcode/{problem_name}/` to `.cache/leetcode/{problem_name}/`
- **Regenerate**: Run `make p-gen PROBLEM={problem_name} FORCE=1`
- **Lint check**: Run `make p-lint PROBLEM={problem_name}`
- **Iterate**: If lint fails, update JSON and regenerate until passes

### 6. Solution Preservation

- Copy `solution.py` from backup to newly generated structure
- Run `make p-test PROBLEM={problem_name}` to verify tests pass
- **If tests fail**: Go back to step 4, update JSON, and iterate until passes

### 7. Cleanup and Restore

- **CRITICAL**: Remove entire newly generated `leetcode/{problem_name}/` directory
- **CRITICAL**: Restore original structure from `.cache/leetcode/{problem_name}/` backup
- **CRITICAL**: Only THEN copy enhanced `test_solution.py` from generated files to restored structure
- **CRITICAL**: Preserve existing solution class parametrization - if original test had multiple solution classes, restore them
- Verify final state with `make p-test PROBLEM={problem_name}`
- Clean up backup directory after successful verification

## Test Case Quality Standards

### Coverage Requirements

- **Minimum 10 test cases** per problem
- **Edge cases**: 20-30% of total test cases
- **Normal cases**: 50-60% of total test cases
- **Corner cases**: 20-30% of total test cases

### Test Case Categories

#### Edge Cases

- Empty inputs: `[]`, `""`, `None`
- Single element: `[1]`, `"a"`
- Boundary values: `[0]`, `[1]`, `[-1]`
- Maximum/minimum constraints from problem description

#### Corner Cases

- Duplicate elements: `[1,1,1]`
- Sorted/reverse sorted arrays: `[1,2,3]`, `[3,2,1]`
- All same elements: `[5,5,5,5]`
- Alternating patterns: `[1,0,1,0]`

#### Normal Cases

- Mixed positive/negative numbers
- Various array sizes within constraints
- Different data patterns and structures
- Representative problem scenarios

### JSON Format Requirements

- Use single quotes for Python strings in test cases
- Follow existing parametrize format
- Maintain type hints in parametrize_typed
- Ensure test_cases string is valid Python list syntax
- **NEVER include custom solution classes** in test_imports - only import the main solution class specified in solution_class_name
- **PRESERVE existing solution class parametrization** - if original test had multiple solution classes, restore them after JSON regeneration

## Commands Reference

```bash
# Find problems needing more test cases
poetry run python .templates/check_test_cases.py --threshold=10 --max=1

# Test specific problem
make p-test PROBLEM={problem_name}

# Generate from JSON template
make p-gen PROBLEM={problem_name} FORCE=1

# Lint specific problem
make p-lint PROBLEM={problem_name}
```

## Error Handling

- **Implementation errors**: Ask user before modifying solution code
- **Test failures**: Update JSON template and regenerate
- **Lint failures**: Fix JSON format and iterate
- **Backup failures**: Ensure `.cache/leetcode/` directory exists

## Success Criteria

- All tests pass with enhanced test cases
- Minimum 10 comprehensive test cases per problem
- Original solution code preserved and working
- JSON template updated for future regeneration
- Clean final state with no temporary files
