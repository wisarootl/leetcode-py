# Cookiecutter Template Modernization Plan

## Analysis Summary

**Target Structure**: `leetcode/.example/` contains the reference implementation
**Key Differences Found:**

- `leetcode/.example/` has `__init__.py` files (missing in old template)
- `leetcode/.example/` uses modern Python syntax (`TreeNode | None` vs `Optional[TreeNode]`)
- `leetcode/.example/` follows project's coding standards more closely
- Template must generate files identical to `leetcode/.example/` structure

## Implementation Plan

### 0. Explicit File Content Analysis

- **Tool**: `.amazonq/plan/compare_template_files.py` (reusable comparison script)
- **Usage**:
    - `python .amazonq/plan/compare_template_files.py template` - Compare reference vs template source
    - `python .amazonq/plan/compare_template_files.py generated` - Compare reference vs generated files
- **Analysis**: Line-by-line diff of all file types
- **Document**: Exact differences and required changes
- **Verify**: Template variables handle all variations

### 1. Incremental Template Updates (File-by-File Approach)

#### Phase 1: Add `__init__.py`

- **Add**: Empty `__init__.py` file to template
- **Validate**: `make q-gen` → `make q-validate` → `make lint`

#### Phase 2: Fix `solution.py`

- **Update**: Modern syntax (`TreeNode | None`), clean template logic
- **Validate**: `make q-gen` → `make q-validate` → `make lint`

#### Phase 3: Fix `tests.py`

- **Update**: Relative imports (`from .solution`), clean structure
- **Validate**: `make q-gen` → `make q-validate` → `make lint`

#### Phase 4: Fix `README.md`

- **Update**: Clean formatting, proper markdown
- **Validate**: `make q-gen` → `make q-validate` → `make lint`

#### Phase 5: Fix `playground.ipynb`

- **Update**: Clean cells without execution state
- **Validate**: `make q-gen` → `make q-validate` → `make lint`

**Benefits**: Isolated debugging, safer progression, easier rollback

### 2. Multi-Problem Type Testing

- **Test Cases**: Ensure template handles all problem types
    - Basic array: `two_sum` (return `list[int]`)
    - Tree: `invert_binary_tree` (return `TreeNode | None`)
    - String: problems returning `str`
    - Boolean: problems returning `bool`
    - No imports vs TreeNode/ListNode imports
- **Validation**: Each type generates correctly

### 3. Modernize cookiecutter.json Schema

- **Base on**: Existing `.templates/leetcode/.example/examples/` JSON5 files
- **Ensure**: All template variables are properly defined
- **Add**: Missing fields found in real examples
- **Note**: Variable mapping handled by `gen.py` `convert_arrays_to_nested()`

### 4. Update Template Files

#### solution.py

- Use modern type hints (`TreeNode | None` not `Optional[TreeNode]`)
- Match exact import patterns from real examples
- Ensure proper TODO placeholder format

#### tests.py

- Follow `@logged_test` decorator pattern
- Use parametrized pytest structure
- Match logging format from real examples

#### README.md

- Follow exact format from real examples
- Include proper problem description formatting

#### playground.ipynb

- Ensure notebook structure matches real examples

### 5. Template Generation Logic

- **File**: `.templates/leetcode/gen.py` (already handles variable mapping)
- **Integration**: Works with `make q-gen QUESTION=name` (verified in Makefile)
- **Update**: Handle new `__init__.py` file
- **Process**: JSON → `gen.py` → cookiecutter → `leetcode/$(QUESTION)/`

### 6. Automated Validation System

- **Tool**: Reusable `.amazonq/plan/compare_template_files.py`
- **Usage**:
    ```bash
    # Validate current template generates correct files
    python .amazonq/plan/compare_template_files.py generated --question=invert_binary_tree
    ```
- **Makefile**: `make q-validate QUESTION=name` (implemented)
- **Test**: Template regression testing
- **Ensure**: `make q-gen` + `make lint` + `make q-test` all pass

### 7. Testing & Validation

- **Test**: Template generation with existing JSON files
- **Verify**: Generated files match `leetcode/.example/` structure exactly
- **Compare**: Automated diff against reference files
- **Ensure**: `make q-gen` works seamlessly
- **Test**: Recreation process from `.prompt/` files
- **Validate**: Multi-problem type generation

## Key Template Variables to Ensure

```json
{
  "question_name": "snake_case_name",
  "class_name": "PascalCaseName",
  "method_name": "snake_case_method",
  "problem_number": "226",
  "problem_title": "Display Title",
  "difficulty": "Easy|Medium|Hard",
  "topics": "Comma, Separated, Topics",
  "tags": ["grind-75", "blind-75"],
  "problem_description": "Full description",
  "examples": [{"input": "...", "output": "..."}],
  "constraints": "Formatted constraints",
  "parameters": "typed_params: list[int]",
  "return_type": "TreeNode | None",
  "imports": "from leetcode_py.tree_node import TreeNode",
  "test_cases": [{"args": [...], "expected": ...}]
}
```

## Success Criteria

### Phase-by-Phase Validation (File-by-File)

1. ✅ **Phase 1**: `__init__.py` files generated correctly
2. ✅ **Phase 2**: `solution.py` with modern syntax (`TreeNode | None`)
3. ✅ **Phase 3**: `tests.py` with relative imports and clean structure
4. ✅ **Phase 4**: `README.md` with clean formatting
5. ✅ **Phase 5**: `playground.ipynb` with clean cells

### Multi-Problem Type Validation

5. ✅ Basic problems (array/string) generate correctly
6. ✅ Tree problems generate correctly
7. ✅ Different return types handled (`bool`, `int`, `str`, `list`, etc.)

### Automated Validation

8. ✅ Automated diff shows no differences vs `leetcode/.example/`
9. ✅ `make q-validate` passes for all problem types
10. ✅ Recreation from `.prompt/` works flawlessly
11. ✅ All linting passes (`make lint`)
12. ✅ Tests run successfully (`make q-test`)

## Files to Modify

### Template Files

1. `.templates/leetcode/{{cookiecutter.question_name}}/`
    - **Add**: `__init__.py` (empty file)
    - **Update**: `solution.py` (modern syntax, imports)
    - **Update**: `tests.py` (match `leetcode/.example/` format)
    - **Update**: `README.md` (match `leetcode/.example/` format)
    - **Update**: `playground.ipynb` (match structure)

### Configuration

2. `.templates/leetcode/cookiecutter.json`
    - Align with JSON5 examples
    - Add missing variables

### Generation Logic

3. `.templates/leetcode/gen.py`
    - Handle `__init__.py` generation
    - Maintain existing variable mapping

### Validation Tools

4. **Reusable**: `.amazonq/plan/compare_template_files.py` (handles both template and generated comparisons)
5. **New**: Makefile target `make q-validate`

## Risk Mitigation

- **Incremental phases** prevent all-or-nothing failures
- **Automated validation** catches regressions immediately
- **Multi-problem testing** ensures template generalization
- **Explicit file comparison** documents exact requirements

## Critical Rule: Reference Directory Protection

**NEVER modify these reference directories:**

- `.templates/leetcode/.example/` - Template reference examples
- `leetcode/.example/` - Generated file reference examples

**ONLY modify the actual template directory:**

- `.templates/leetcode/{{cookiecutter.question_name}}/` - The actual cookiecutter template

**Workflow**: Modify template → Generate (`make q-gen`) → Compare vs reference (`make q-validate`)

This plan ensures the template generates files that exactly match `leetcode/.example/` while maintaining the robust generation process described in the rules.
