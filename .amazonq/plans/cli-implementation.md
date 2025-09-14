# CLI Implementation Plan

## Overview

Transform `leetcode-py` from a local development repository into a PyPI-installable CLI tool that allows users to generate LeetCode problems in any directory.

## Target CLI Interface

```bash
# Install from PyPI
pip install leetcode-py-sdk

# Generate problems (with short options)
lcpy gen -n 1                    # or --problem-num=1
lcpy gen -s two-sum             # or --problem-slug=two-sum
lcpy gen -t grind-75            # or --problem-tag=grind-75
lcpy gen -n 1 -o my-problems     # Custom output directory (default: leetcode/)

# Scrape problems (with short options)
lcpy scrape -n 1                # or --problem-num=1
lcpy scrape -s two-sum          # or --problem-slug=two-sum

# List problems
lcpy list
lcpy list --tag=grind-75
lcpy list --difficulty=easy
```

## Current State Analysis

### ✅ Already Available

- **Core functionality**: Scraping (`LeetCodeScraper`), generation (`TemplateGenerator`), parsing (`HTMLParser`)
- **Data structures**: `TreeNode`, `ListNode`, `GraphNode`, `DictTree`
- **Template system**: Cookiecutter templates in `.templates/leetcode/`
- **JSON problem definitions**: 75+ problems in `.templates/leetcode/json/`
- **Tag system**: Problems have `_tags.list` field (e.g., `["grind-75"]`)
- **Dependencies**: `typer`, `requests`, `cookiecutter` already in `pyproject.toml`

### ❌ Missing Components

- **CLI entry point**: No `lcpy` command defined
- **Tag-based bulk generation**: No logic to find problems by tag
- **List command**: No way to browse available problems
- **Package resources**: Templates not packaged for distribution
- **Working directory generation**: Currently generates in fixed `leetcode/` folder

## Implementation Steps

### 1. Package Structure Refactoring

**Current**: Templates as files in `.templates/`
**Target**: Templates as package resources

```
leetcode_py/
├── cli/
│   ├── __init__.py
│   ├── main.py          # Main CLI entry point
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── gen.py       # Generation commands
│   │   ├── list.py      # List commands
│   │   └── scrape.py    # Scraping commands (moved from .templates/)
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── problem_finder.py
│   │   └── check_test_cases.py  # Moved from .templates/
│   └── resources/       # Package resources
│       └── .templates/  # Template data only
│           └── leetcode/
│               ├── {{cookiecutter.problem_name}}/
│               ├── json/
│               ├── examples/
│               └── cookiecutter.json
├── tools/               # Existing scraper/generator
└── data_structures/     # Existing data structures
```

### 2. CLI Entry Point Setup

**File**: `pyproject.toml`

```toml
[tool.poetry.scripts]
lcpy = "leetcode_py.cli.main:app"
```

### 3. Core CLI Implementation

**File**: `leetcode_py/cli/main.py`

```python
import typer
from .commands import gen, scrape, list_cmd

app = typer.Typer(help="LeetCode problem generator")
app.add_typer(gen.app, name="gen")
app.add_typer(scrape.app, name="scrape")
app.add_typer(list_cmd.app, name="list")
```

**File**: `leetcode_py/cli/commands/gen.py`

```python
import typer
from typing import Optional
from pathlib import Path

app = typer.Typer(help="Generate LeetCode problems")

@app.command()
def generate(
    problem_num: Optional[int] = typer.Option(None, "-n", "--problem-num", help="Problem number"),
    problem_slug: Optional[str] = typer.Option(None, "-s", "--problem-slug", help="Problem slug"),
    problem_tag: Optional[str] = typer.Option(None, "-t", "--problem-tag", help="Problem tag (bulk)"),
    output: str = typer.Option("leetcode", "-o", "--output", help="Output directory (default: leetcode)")
):
    # Validation: exactly one of problem_num/problem_slug/problem_tag required
    # Implementation: use existing scraper/generator
    # Generate in specified output directory (default: leetcode/)
```

### 4. Tag-Based Problem Discovery

**File**: `leetcode_py/cli/utils/problem_finder.py`

```python
def find_problems_by_tag(tag: str) -> list[str]:
    """Find all problem JSON files containing the specified tag."""
    # Scan package resources for JSON files
    # Parse _tags.list field
    # Return list of problem names
```

### 5. Scrape Command Implementation

**File**: `leetcode_py/cli/commands/scrape.py`

```python
import typer
from typing import Optional
from leetcode_py.tools import LeetCodeScraper

app = typer.Typer(help="Scrape LeetCode problems")

@app.command()
def fetch(
    problem_num: Optional[int] = typer.Option(None, "-n", "--problem-num", help="Problem number"),
    problem_slug: Optional[str] = typer.Option(None, "-s", "--problem-slug", help="Problem slug")
):
    # Validation: exactly one option required
    # Implementation: use existing LeetCodeScraper
    # Output JSON to stdout
```

### 6. List Command Implementation

**File**: `leetcode_py/cli/commands/list.py`

```python
import typer
from typing import Optional

app = typer.Typer(help="List LeetCode problems")

@app.command()
def problems(
    tag: Optional[str] = typer.Option(None, "-t", "--tag", help="Filter by tag"),
    difficulty: Optional[str] = typer.Option(None, "-d", "--difficulty", help="Filter by difficulty")
):
    # List available problems with filtering
    # Display: number, title, difficulty, tags
```

### 7. JSON Data Structure Design

**Proposed JSON Structure**:

```
.templates/leetcode/json/
├── problems/              # Individual problem definitions
│   ├── two_sum.json
│   ├── valid_palindrome.json
│   └── ...
├── tags.json5            # Single source of truth for tags (with comments)
├── number_to_slug.json   # Auto-generated mapping
└── metadata.json         # Auto-generated repository metadata
```

**Core Files**:

1. **`tags.json5`** - Single Source of Truth (with comments)

```json5
{
    // Core study plans
    "grind-75": ["two_sum", "valid_palindrome", "merge_two_sorted_lists"],

    // Extended grind (169 problems total)
    grind: [
        { tag: "grind-75" }, // Include all grind-75 problems
        "additional_problem_1",
        "additional_problem_2",
    ],

    // Original blind 75 problems
    "blind-75": ["two_sum", "longest_substring_without_repeating_characters"],

    // NeetCode 150 (overlaps with grind-75)
    "neetcode-150": [
        { tag: "grind-75" }, // Include grind-75 as base
        "contains_duplicate",
        "group_anagrams",
    ],
}
```

2. **`number_to_slug.json`** - Auto-generated

```json
{
    "1": "two_sum",
    "125": "valid_palindrome",
    "21": "merge_two_sorted_lists"
}
```

3. **`metadata.json`** - Auto-generated Repository Info

```json
{
    "version": "1.0.0",
    "total_problems": 75,
    "last_updated": "2024-01-15T10:30:00Z",
    "difficulty_counts": {
        "Easy": 25,
        "Medium": 35,
        "Hard": 15
    },
    "tag_counts": {
        "grind-75": 75,
        "grind": 169,
        "neetcode-150": 150
    }
}
```

**Auto-generation Logic**:

- `total_problems`: Count files in `problems/`
- `difficulty_counts`: Parse `difficulty` field from all problem JSONs
- `tag_counts`: Resolve tag references and count unique problems per tag
- `last_updated`: Current timestamp
- `version`: From `pyproject.toml` or git tag

**Pre-commit Automation**:

```yaml
- repo: local
  hooks:
      - id: sync-problem-tags
        name: Sync problem tags from tags.json
        entry: poetry run python scripts/sync_tags.py
        language: system
        files: "^.templates/leetcode/json/(tags.json5|problems/.+.json)$"

      - id: generate-mappings
        name: Generate number-to-slug mapping
        entry: poetry run python scripts/generate_mappings.py
        language: system
        files: "^.templates/leetcode/json/problems/.+.json$"

      - id: update-metadata
        name: Update metadata.json
        entry: poetry run python scripts/update_metadata.py
        language: system
        files: "^.templates/leetcode/json/problems/.+.json$"
```

### 8. Resource Packaging

**Migration Steps**:

1. **Template resources**: Move `.templates/leetcode/` → `leetcode_py/cli/resources/.templates/leetcode/`
    - Includes: `{{cookiecutter.problem_name}}/`, `json/`, `examples/`, `cookiecutter.json`
2. **CLI functionality**: Refactor existing scripts into CLI commands
    - `.templates/leetcode/gen.py` → integrate into `leetcode_py/cli/commands/gen.py`
    - `.templates/leetcode/scrape.py` → `leetcode_py/cli/commands/scrape.py` (update args to match gen format)
    - `.templates/check_test_cases.py` → `leetcode_py/cli/utils/check_test_cases.py`

**Scrape Command Compatibility**: Update scrape.py arguments to match gen command format:

```python
# Current: scrape.py -n 1 or -s two-sum
# Target:  lcpy scrape --problem-num=1 or --problem-slug=two-sum
#         lcpy scrape -n 1 or -s two-sum (short versions)
```

**Short Option Support**: All commands support short flags:

- `-n` for `--problem-num` (number) - gen, scrape
- `-s` for `--problem-slug` (slug) - gen, scrape
- `-t` for `--problem-tag` (tag) - gen only
- `-o` for `--output` (output directory) - gen only
- `-t` for `--tag` (filter) - list only
- `-d` for `--difficulty` (filter) - list only

3. Update `pyproject.toml` to include package data:

```toml
[tool.poetry]
packages = [{include = "leetcode_py"}]
include = ["leetcode_py/cli/resources/**/*"]
```

**Why `include` is needed**: Poetry only packages `.py` files by default. The `include` directive ensures non-Python files (`.json`, `.md`, `.ipynb`) in the templates are packaged.

### 9. Working Directory Generation

**Current**: Fixed output to `leetcode/` folder
**Target**: Configurable output directory with `--output` option

**Changes needed**:

- Modify `TemplateGenerator` to accept output directory parameter
- CLI commands generate in specified `--output` (default: `leetcode/`)
- Update cookiecutter template paths to use package resources
- Support both relative and absolute paths

### 10. Dependency Management

**Move to main dependencies** (from dev):

- `cookiecutter` - needed for template generation
- Keep `typer`, `requests` in main dependencies

**Update `pyproject.toml`**:

```toml
[tool.poetry.dependencies]
python = "^3.13"
graphviz = "^0.21"
requests = "^2.32.5"
typer = "^0.17.0"
cookiecutter = "^2.6.0"  # Move from dev
json5 = "^0.9.0"  # For parsing tags.json5 with comments
```

### 11. Testing Strategy

**New test files**:

- `tests/cli/test_main.py` - CLI entry point tests
- `tests/cli/test_gen.py` - Generation command tests
- `tests/cli/test_scrape.py` - Scrape command tests
- `tests/cli/test_list.py` - List command tests
- `tests/cli/test_problem_finder.py` - Tag discovery tests

**Test approach**:

- Use `typer.testing.CliRunner` for CLI testing
- Mock file system operations
- Test resource loading from package

### 12. Documentation Updates

**Files to update**:

- `README.md` - Add installation and CLI usage sections
- `.amazonq/rules/problem-creation.md` - Update for CLI workflow
- Add `docs/cli-usage.md` - Comprehensive CLI documentation

## Migration Strategy

### Phase 1: Core CLI Structure ✅ COMPLETED

1. ✅ Create `leetcode_py/cli/` package structure
    - Created `leetcode_py/cli/main.py` with typer app
    - Added `leetcode_py/cli/commands/` and `leetcode_py/cli/utils/` packages
2. ✅ Implement basic CLI entry point with typer
    - Dynamic version detection using `importlib.metadata.version()`
    - Clean `--version/-V` flag without callback overhead
    - Placeholder commands: `gen`, `scrape`, `list`
3. ✅ Add CLI script to `pyproject.toml`
    - Entry point: `lcpy = "leetcode_py.cli.main:main"`
4. ✅ Test basic `lcpy --help` functionality
    - Comprehensive test suite: 8 tests covering help, version, commands, error handling
    - All tests pass (1438 total: 1430 existing + 8 new CLI tests)

### Phase 2: Resource Packaging ✅ COMPLETED

1. ✅ Move templates and JSON files to package resources
    - Copied `.templates/leetcode/` → `leetcode_py/cli/resources/leetcode/`
    - Updated `pyproject.toml` to include resources with `include = ["leetcode_py/cli/resources/**/*"]`
2. ✅ Update resource loading in existing tools
    - Created `leetcode_py/cli/utils/resources.py` for resource access
    - Updated `TemplateGenerator` to use packaged resources with fallback to local development
    - Moved `cookiecutter` and `json5` to main dependencies
3. ✅ Test template generation from package resources
    - Verified template generation works with both local and packaged resources
    - All CLI tests pass (8/8)
    - Template generation creates all expected files (solution.py, test_solution.py, etc.)

### Phase 3: Gen Command Implementation ✅ COMPLETED

1. ✅ Implement `lcpy gen -n N` (with `--problem-num` long form)
    - Created `leetcode_py/cli/commands/gen.py` with number-based generation
    - Added `find_problem_by_number()` utility for number-to-name mapping
2. ✅ Implement `lcpy gen -s NAME` (with `--problem-slug` long form)
    - Direct slug-based generation using existing JSON files
3. ✅ Implement `lcpy gen -t TAG` (with `--problem-tag` long form)
    - Bulk generation by tag with progress feedback
    - Shows count of problems found for the tag
4. ✅ Add tag discovery utilities with centralized tags.json5
    - Created `tags.json5` with grind-75, blind-75, easy tags
    - Implemented `find_problems_by_tag()` using json5 parsing
5. ✅ Add resource loading for packaged templates
    - Created `leetcode_py/cli/utils/resources.py` for template access
    - Supports both development and packaged resource paths
6. ✅ Comprehensive testing
    - 8 test cases covering all generation modes and error conditions
    - All tests pass with proper error handling validation

### Phase 4: Scrape Command Implementation ✅ COMPLETED

1. ✅ Implement `lcpy scrape -n N` (with `--problem-num` long form)
2. ✅ Implement `lcpy scrape -s NAME` (with `--problem-slug` long form)
3. ✅ Integrate existing `LeetCodeScraper` with CLI interface
4. ✅ Output JSON to stdout with proper formatting
5. ✅ Comprehensive testing with 8 test cases covering all scenarios
6. ✅ Proper error handling for invalid inputs and network failures

### Phase 5: List Commands

1. Implement `lcpy list` basic functionality
2. Add filtering: `lcpy list -t grind-75` and `lcpy list -d easy`
3. Format output for readability (table format with number, title, difficulty, tags)

### Phase 6: Testing & Documentation

1. Add comprehensive CLI tests
2. Update documentation
3. Test PyPI packaging workflow

## Implementation Notes

### Phase 1 Key Decisions

**Version Handling**:

- Uses `importlib.metadata.version('leetcode-py')` for dynamic version detection
- Works in both development (poetry install) and production (pip install) environments
- Wrapped in `show_version()` function for clean separation of concerns

**CLI Architecture**:

- Avoided callback-based version handling to prevent unnecessary function calls on every command
- Used `invoke_without_command=True` with manual help display for better control
- Clean parameter naming: `version_flag` instead of `version` to avoid naming conflicts

**Testing Strategy**:

- Comprehensive test coverage for all CLI functionality
- Tests expect exit code 0 for help display (not typer's default exit code 2)
- Dynamic version testing (checks for "lcpy version" presence, not hardcoded version)

**Code Quality**:

- Removed noise docstrings following development rules
- Minimal imports and clean function separation
- No `if __name__ == "__main__"` block needed (handled by pyproject.toml entry point)

### Phase 2 Key Decisions

**Resource Packaging Strategy**:

- Used `importlib.resources` for cross-platform package resource access
- Implemented fallback mechanism: local development → packaged resources → final fallback
- Added `include` directive in `pyproject.toml` to package non-Python files

**Dependency Management**:

- Moved `cookiecutter` from dev to main dependencies (needed for CLI functionality)
- Added `json5` for future tags.json5 support with comments
- Maintained backward compatibility with existing tools

**Template Generation**:

- Updated `TemplateGenerator` to accept optional `template_dir` and `output_dir` parameters
- Maintained existing API while adding package resource support
- Verified generation works in both development and packaged environments

## Success Criteria

- [ ] `pip install leetcode-py-sdk` installs CLI globally
- [ ] `lcpy gen -n 1` generates Two Sum in default `leetcode/` directory
- [ ] `lcpy gen -n 1 -o my-problems` generates Two Sum in `my-problems/` directory
- [ ] `lcpy gen -s two-sum` works identically
- [ ] `lcpy gen -t grind-75` generates all 75 problems with tag resolution
- [ ] `lcpy scrape -n 1` outputs Two Sum JSON data
- [ ] `lcpy scrape -s two-sum` works identically
- [ ] `lcpy list` shows all available problems in table format
- [ ] `lcpy list -t grind-75` filters correctly
- [ ] `lcpy list -d easy` filters by difficulty
- [ ] Generated problems maintain same structure as current repo
- [ ] All existing data structures (`TreeNode`, etc.) remain importable
- [ ] CLI works from any directory
- [ ] Package size reasonable for PyPI distribution

## Risk Mitigation

**Resource Loading**: Test package resource access across different Python environments
**Template Compatibility**: Ensure cookiecutter templates work from package resources
**Working Directory**: Verify generation works correctly in various directory structures
**Backward Compatibility**: Maintain existing API for users who import `leetcode_py` directly

## Timeline Estimate

- **Phase 1-2**: 2-3 days (CLI structure + resource packaging)
- **Phase 3**: 1-2 days (gen command implementation)
- **Phase 4**: 1-2 days (scrape command implementation)
- **Phase 5**: 1-2 days (list commands)
- **Phase 6**: 2-3 days (testing + documentation)

**Total**: ~1-2 weeks for complete implementation
