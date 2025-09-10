# Cookiecutter Template Generalization Plan

## Current Issues Identified

### 1. **Template Constraint Issues**

- `first_bad_version/solution.py`: Has `# TODO: template constraint` - needs custom `__init__` method
- Template doesn't support constructor parameters or custom initialization logic
- No support for API mocking patterns (like `isBadVersion`)

### 2. **Limited Method Flexibility**

- No support for static methods, class methods, or property decorators
- Missing support for optional parameters with defaults
- No support for method overloading patterns
- Cannot handle methods that don't need `self` parameter

### 3. **Complex Test Patterns Not Supported**

- Design problems need operation sequences (LRU Cache pattern)
- Interactive problems need API mocking (First Bad Version)
- Some problems need custom helper methods in tests
- No support for test fixtures or complex setup

### 4. **Playground Notebook Limitations**

- Fixed 4-cell structure doesn't fit all problem types
- No support for visualization cells
- Missing support for interactive debugging
- Cannot handle complex setup requirements
- **Import conflicts**: Cannot import `tests.py` due to root-level `tests/` directory conflict
- **Missing test helpers**: Need access to test utility functions like `create_cycle_list` in notebooks
- **Path manipulation required**: Manual `sys.path` modifications needed for imports

### 5. **Missing Template Variants**

- No support for multiple solution approaches in one file
- Missing templates for specific problem categories (graph, trie, etc.)
- No support for helper classes or data structures
- Cannot generate algorithm explanation comments

## Proposed Solutions

### Phase 1: Template Structure Improvements

#### 1.1 Enhanced Method Configuration

```json
"solution_methods": [
    {
        "name": "method_name",
        "parameters": "param1: type1, param2: type2 = default",
        "return_type": "ReturnType",
        "dummy_return": "default_value",
        "decorators": ["@staticmethod", "@classmethod", "@property"],
        "is_constructor": true,
        "time_complexity": "O(n)",
        "space_complexity": "O(1)",
        "algorithm_notes": "Brief explanation"
    }
]
```

#### 1.2 Flexible Template Structure

```jinja2
{%- for method in solution_methods %}
{%- if method.decorators %}
{%- for decorator in method.decorators %}
    {{ decorator }}
{%- endfor %}
{%- endif %}
    # Time: {{ method.time_complexity or "O(?)" }}
    # Space: {{ method.space_complexity or "O(?)" }}
{%- if method.is_constructor %}
    def {{ method.name }}(self{% if method.parameters %}, {{ method.parameters }}{% endif %}){% if method.return_type %} -> {{ method.return_type }}{% endif %}:
{%- else %}
    def {{ method.name }}({% if not method.decorators or "@staticmethod" not in method.decorators %}self{% if method.parameters %}, {% endif %}{% endif %}{{ method.parameters or "" }}){% if method.return_type %} -> {{ method.return_type }}{% endif %}:
{%- endif %}
{%- if method.algorithm_notes %}
        # {{ method.algorithm_notes }}
{%- endif %}
        # TODO: Implement {{ method.name }}
{%- if method.dummy_return %}
        return {{ method.dummy_return }}
{%- endif %}
{%- endfor %}
```

### Phase 2: Test Template Enhancements

#### 2.1 Flexible Test Patterns

```json
"test_patterns": {
    "type": "basic|design|interactive|tree|graph",
    "setup_complexity": "simple|complex|custom",
    "assertion_type": "direct|tree_comparison|operation_sequence"
}
```

#### 2.2 Enhanced Test Methods

```json
"test_methods": [
    {
        "name": "test_method",
        "pattern": "parametrized|custom|fixture",
        "setup_code": "custom setup if needed",
        "parametrize": "params",
        "test_cases": "test data",
        "body": "test logic",
        "cleanup_code": "optional cleanup"
    }
]
```

### Phase 3: Notebook Template Flexibility

#### 3.1 Dynamic Cell Structure

```json
"notebook_cells": [
    {
        "id": "imports",
        "type": "code",
        "content": "{{ playground_imports }}"
    },
    {
        "id": "setup",
        "type": "code",
        "content": "{{ playground_setup }}"
    },
    {
        "id": "visualization",
        "type": "code",
        "content": "{{ playground_visualization }}",
        "optional": true
    },
    {
        "id": "execute",
        "type": "code",
        "content": "{{ playground_execution }}"
    },
    {
        "id": "test",
        "type": "code",
        "content": "{{ playground_assertion }}"
    }
]
```

#### 3.2 Test Helper Integration

```json
"notebook_config": {
    "needs_test_helpers": true,
    "helper_functions": ["create_cycle_list", "build_tree", "create_graph"],
    "import_strategy": "helpers_file|inline_helpers|test_utils"
}
```

### Phase 4: Problem-Specific Templates

#### 4.1 Template Categories

- **Basic**: Array, string, number problems
- **Design**: Data structure implementation (LRU Cache, Trie)
- **Interactive**: Problems with external APIs (First Bad Version)
- **Tree**: Binary tree problems with visualization
- **Graph**: Graph problems with node structures
- **Algorithm**: Complex algorithms with step-by-step breakdown

#### 4.2 Category-Specific Fields

```json
"template_category": "design",
"design_config": {
    "operation_methods": ["get", "put", "delete"],
    "test_operation_sequence": true,
    "supports_multiple_instances": true
},
"interactive_config": {
    "external_apis": ["isBadVersion"],
    "mock_setup_required": true
},
"tree_config": {
    "visualization_enabled": true,
    "supports_null_nodes": true
}
```

## Implementation Plan

### Step 1: Backup and Analysis (Week 1)

- [ ] Create backup of current template
- [ ] Analyze all 70+ existing problems for patterns
- [ ] Document current template limitations
- [ ] Create test cases for new template features

### Step 2: Core Template Enhancement (Week 2)

- [ ] Implement enhanced method configuration
- [ ] Add support for decorators and special methods
- [ ] Update solution.py template with flexibility
- [ ] Add algorithm complexity and notes support

### Step 3: Test Template Improvements (Week 3)

- [ ] Implement flexible test patterns
- [ ] Add support for design problem test sequences
- [ ] Add interactive problem mocking support
- [ ] Update tests.py template

### Step 4: Notebook Template Enhancement (Week 4)

- [ ] Implement dynamic cell structure
- [ ] Add visualization cell support
- [ ] Add debugging and exploration cells
- [ ] **Solve import conflicts**: Create `helpers.py` pattern for test utilities
- [ ] **Clean imports**: Remove need for manual `sys.path` manipulation
- [ ] **Test helper access**: Provide clean access to test utility functions
- [ ] Update playground.ipynb template

### Step 5: Category-Specific Templates (Week 5)

- [ ] Create template variants for each category
- [ ] Implement category-specific configuration
- [ ] Add template selection logic to generator
- [ ] Update JSON schema validation

### Step 6: Migration and Testing (Week 6)

- [ ] Test new template with existing problems
- [ ] Create migration script for existing JSONs
- [ ] Update documentation and examples
- [ ] Validate all generated problems pass linting

## Success Criteria

1. **Template Flexibility**: Support all current problem types without manual fixes
2. **Zero Manual Intervention**: Generated code should pass `make p-lint` immediately
3. **Backward Compatibility**: Existing JSON files should work with new template
4. **Enhanced Features**: Support for decorators, complex tests, and visualizations
5. **Category Support**: Automatic template selection based on problem type

## Risk Mitigation

1. **Breaking Changes**: Maintain backward compatibility with existing JSONs
2. **Complexity**: Keep template readable with clear documentation
3. **Performance**: Ensure generation time remains fast
4. **Maintenance**: Create comprehensive test suite for template validation

## Files to Modify

### Core Template Files

- `.templates/leetcode/{{cookiecutter.problem_name}}/solution.py`
- `.templates/leetcode/{{cookiecutter.problem_name}}/tests.py`
- `.templates/leetcode/{{cookiecutter.problem_name}}/playground.ipynb`
- **Add**: `.templates/leetcode/{{cookiecutter.problem_name}}/helpers.py` (conditional)
- `.templates/leetcode/cookiecutter.json`

### Generator Logic

- `leetcode_py/tools/generator.py`
- `.templates/leetcode/gen.py`

### Examples and Documentation

- `.templates/leetcode/examples/basic.json5`
- `.templates/leetcode/examples/design.json5`
- Add: `.templates/leetcode/examples/interactive.json5`
- Add: `.templates/leetcode/examples/tree.json5`
- Add: `.templates/leetcode/examples/graph.json5`

### Validation and Testing

- Add: `.templates/leetcode/validate_template.py`
- Add: `tests/templates/test_template_generation.py`

## Notebook Import Issue Solutions

### Option 1: Dedicated `helpers.py` File (Recommended)

- Generate `helpers.py` when `needs_test_helpers: true`
- Extract reusable functions from test class
- Clean imports: `from helpers import create_cycle_list`
- No path manipulation needed

### Option 2: Enhanced Test Utils

- Add problem-specific helpers to `leetcode_py.test_utils`
- Import: `from leetcode_py.test_utils import create_cycle_list`
- Centralized but may become bloated

### Option 3: Inline Helper Functions

- Generate helper functions directly in notebook setup cell
- Self-contained but duplicates code
- Good for simple helpers

**Chosen Approach**: Option 1 with conditional generation based on problem type.

This plan addresses all identified template limitations while maintaining backward compatibility and adding powerful new features for different problem categories.
