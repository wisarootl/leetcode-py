# Plan: Regenerate All Problems with Fresh LeetCode Data

## Overview

Scrape fresh data from LeetCode for existing problems and generate new JSON files using the new universal cookiecutter template, ensuring all generated code passes linting.

## Current State Analysis

- Old JSON files: `.templates/leetcode/old/template/json/*.json` (for problem names only)
- Scraper: `.templates/leetcode/scrape.py` (existing)
- New template: `.templates/leetcode/cookiecutter.json` + templates
- Target: `.templates/leetcode/json/*.json` (new format with fresh data)
- Generated problems: `leetcode/*/`

## Phase 1: Extract Problem Names

### 1.1 Get Problem Names from Old JSON

```bash
ls .templates/leetcode/old/template/json/
```

Expected problems:

- container_with_most_water.json
- insert_interval.json
- invert_binary_tree.json
- lru_cache.json
- reverse_linked_list_ii.json
- spiral_matrix.json

### 1.2 Extract Problem Numbers/Slugs

From old JSON files, extract:

- Problem numbers (for scraping by number)
- Problem names/slugs (for scraping by slug)

## Phase 2: Create Fresh Scraping Script

### 2.1 Use Existing Scraper

Following the problem creation rules:

```bash
# Fetch by number
poetry run python .templates/leetcode/scrape.py -n 1

# Fetch by slug
poetry run python .templates/leetcode/scrape.py -s "two-sum"
```

### 2.2 Scraping Script: `scrape_all_problems.py`

✅ **Created** - Uses existing scraper to fetch fresh data for all problems

## Phase 3: Execute Fresh Scraping

### 3.1 Run Scraping Script

```bash
cd .templates/leetcode
python scrape_all_problems.py
```

### 3.2 Transform JSON to New Template Format

The scraper creates JSON in new template format automatically.

### 3.3 Verify New JSON Files

```bash
ls .templates/leetcode/json/
# Should show all freshly scraped JSON files
```

## Phase 4: Test Generation Pipeline

### 4.1 Test Single Problem Generation

```bash
make p-gen PROBLEM=container_with_most_water FORCE=1
```

### 4.2 Verify Generated Structure

```bash
ls leetcode/container_with_most_water/
# Should show: __init__.py, solution.py, tests.py, README.md, playground.ipynb
```

### 4.3 Test Linting on Single Problem

```bash
make lint
# Should pass without errors
```

## Phase 5: Full Regeneration

### 5.1 Update Makefile (if needed)

Verify `gen-all-problems` target works with new template:

```makefile
gen-all-problems:
	@echo "This will DELETE all existing problems and regenerate from JSON templates."
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "Deleting existing problems..."
	@rm -rf leetcode/*/
	@echo "Generating all problems..."
	@for json_file in .templates/leetcode/json/*.json; do \
		problem=$$(basename "$$json_file" .json); \
		echo "Generating: $$problem"; \
		poetry run python .templates/leetcode/gen.py "$$json_file" --force; \
	done
```

### 5.2 Run Full Regeneration

```bash
make gen-all-problems FORCE=1
```

### 5.3 Verify All Problems Generated

```bash
ls leetcode/
# Should show all problem directories
```

## Phase 6: Validation & Iteration

### 6.1 Run Linting on All Problems

```bash
make lint
```

### 6.2 Fix Issues (Iterative Process)

**If linting fails:**

1. **Identify Issue Type:**
    - Template formatting issues → Fix template files
    - JSON data issues → Re-scrape or manually fix JSON
    - Import issues → Fix template imports

2. **Fix and Regenerate:**

    ```bash
    # Fix issue in template or JSON
    make gen-all-problems FORCE=1
    make lint
    ```

3. **Repeat until clean:**
    - Continue iteration until `make lint` passes
    - Ensure reproducible generation

### 6.3 Common Issues & Fixes

**Template Issues:**

- Indentation problems → Fix Jinja2 `indent` filters in templates
- Missing imports → Update template import generation
- Method signatures → Fix solution_methods in JSON

**JSON Issues:**

- Missing required fields → Re-scrape with updated scraper
- Incorrect data types → Fix scraper output format
- Test case format → Update scraper test case generation

## Phase 7: Validation Testing

### 7.1 Test Individual Problems

```bash
make p-test PROBLEM=container_with_most_water
make p-test PROBLEM=lru_cache
make p-test PROBLEM=invert_binary_tree
```

### 7.2 Run Full Test Suite

```bash
make test
```

### 7.3 Verify Notebooks Work

- Check playground.ipynb files can be opened
- Verify cell content is properly formatted

## Success Criteria

1. ✅ All old JSON files migrated to new format
2. ✅ `make gen-all-problems` works with new template
3. ✅ All generated problems pass `make lint`
4. ✅ All generated problems pass `make test`
5. ✅ Generation is reproducible (no manual fixes needed)
6. ✅ All problem types work (basic, design, tree, linked list)

## Implementation Order

1. **Create scraping script** - Get fresh data from LeetCode
2. **Run fresh scraping** - Generate new JSON files
3. **Test single problem** - Verify pipeline works
4. **Fix template issues** - Ensure clean generation
5. **Run full regeneration** - Generate all problems
6. **Iterate on linting** - Fix issues until clean
7. **Final validation** - Test all problems work

## Rollback Plan

If issues arise:

1. Keep old template in `.templates/leetcode/old/`
2. Can revert to old generation method
3. New template is additive, doesn't break existing workflow

## Notes

- Focus on reproducible generation without manual intervention
- Prioritize linting compliance over perfect formatting
- Document any template limitations discovered during migration
- Ensure backward compatibility with existing JSON structure
