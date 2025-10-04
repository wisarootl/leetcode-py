# Batch Problem Creation Command

## Assistant Workflow

When user requests **batch creation of multiple problems**, the assistant will:

1. **Get count from user** (default: 5 problems)
2. **Loop through each problem** following the complete workflow
3. **For each problem**:
    - Find next problem via `poetry run python .cursor/.dev/next_problem.py`
    - Follow all steps from `.cursor/commands/problem-creation.md`
    - **MANDATORY**: Read and follow `.cursor/commands/test-quality-assurance.md` for quality verification
4. **Provide batch summary** at the end

**CRITICAL INSTRUCTION**: You MUST read the test-quality-assurance.md file before executing quality assurance for any problem. Do not rely on memory or assumptions about the workflow.

## High-Level Process

### Step 1: Initialize Batch

- Ask user for count (default: 5)
- Confirm batch creation parameters
- Set up progress tracking

### Step 2: Problem Creation Loop

For each problem (1 to count):

#### 2.1: Find Next Problem

```bash
poetry run python .cursor/.dev/next_problem.py
```

- Extract problem number and name from output
- Log progress: "Problem X/Count: #NUMBER - NAME"
- **Note**: The script automatically excludes unscrapable problems (premium, API issues, etc.)

#### 2.2: Follow Problem Creation Workflow

Execute complete workflow from `.cursor/commands/problem-creation.md`:

1. **Scrape** problem data using `poetry run lcpy scrape`
2. **Transform** data into proper JSON template format
3. **Include images** - Extract image URLs and add to readme_examples
4. **Create** JSON file in `leetcode_py/cli/resources/leetcode/json/problems/{problem_name}.json`
5. **Update** Makefile with `PROBLEM ?= {problem_name}`
6. **Generate** problem structure using `make p-gen`
7. **Verify** with `make p-lint` and fix template issues
8. **Iterate** if needed: re-run `make p-gen PROBLEM={problem_name} FORCE=1` and `make p-lint`

#### 2.3: Implement Optimal Solution

**CRITICAL**: Before running quality assurance, implement the optimal solution:

1. **Implement solution**: Write the optimal algorithm in `solution.py`
2. **Add multiple approaches**: Include alternative solutions (e.g., Solution, SolutionOptimized)
3. **Use parametrized testing**: Ensure all solution approaches are tested
4. **Verify correctness**: Solution must handle all test cases correctly

#### 2.4: Quality Assurance & Reproducibility Verification

**MANDATORY**: You MUST read and follow the complete workflow from `.cursor/commands/test-quality-assurance.md` for EVERY problem.

**REQUIRED ACTION**: Before proceeding with quality assurance, you MUST:

1. **Read the file**: `read_file /Users/wisl/Desktop/vault/personal-repo/leetcode-py/.cursor/commands/test-quality-assurance.md`
2. **Follow the exact 4-step process** described in that file
3. **Execute each step** as specified in the test-quality-assurance.md workflow

**CRITICAL**: Do NOT proceed without reading the test-quality-assurance.md file first. The workflow includes specific backup, regenerate, and restore steps that must be followed exactly.

### Step 3: Batch Summary

Provide comprehensive summary:

- Total problems created
- Success rate
- Failed problems (if any) with reasons
- Time taken
- Next steps for any failures

## Example Assistant Response

```
I'll help you create 5 problems in batch. Let me start the process:

=== Batch Problem Creation Started ===
Creating 5 problems...

=== Problem 1/5 ===
Finding next problem...
Running: poetry run python .cursor/.dev/next_problem.py
Next problem: Problem #123 - Word Ladder
Processing: #123 - Word Ladder

Following problem creation workflow:
1. Scraping problem data...
   Running: poetry run lcpy scrape -n 123
   ✓ Scraped successfully

2. Creating JSON template...
   ✓ JSON template created with images included
   ✓ Saved to leetcode_py/cli/resources/leetcode/json/problems/word_ladder.json

3. Updating Makefile...
   ✓ Updated PROBLEM ?= word_ladder

4. Generating problem structure...
   Running: make p-gen PROBLEM=word_ladder
   ✓ Problem structure generated

5. Verifying with linting...
   Running: make p-lint PROBLEM=word_ladder
   ✓ Linting passed

6. Implementing optimal solution...
   ✓ Solution implemented with multiple approaches
   ✓ Parametrized testing configured

7. Running quality assurance...
   Running: make p-test PROBLEM=word_ladder
   ✓ Tests passed (15 test cases)
   ✓ Quality assurance completed

=== Problem 2/5 ===
[Continue with same process...]

=== Batch Summary ===
Total Problems Created: 5/5
Success Rate: 100%
Failed Problems: None
Time Taken: 12 minutes
Next Steps: All problems created successfully!

=== Batch Problem Creation Completed ===
```

## Error Handling

### If a problem fails:

1. **Log the failure** with specific reason
2. **Continue with next problem** (don't stop the batch)
3. **Add to retry list** for manual intervention later
4. **Update success rate** accordingly

### Common failure scenarios:

- Scraping fails (problem not found, premium problem, API issues)
- JSON template issues (invalid syntax)
- Generation fails (missing dependencies)
- Tests fail (incorrect expected values)
- Linting errors (template problems)
- Unscrapable problems (automatically excluded by next_problem.py)

### Recovery actions:

- **Scraping**: Try alternative parameters or manual data entry
- **JSON**: Fix syntax and regenerate
- **Generation**: Check Makefile and dependencies
- **Tests**: Update expected values in JSON template
- **Linting**: Fix template issues and regenerate
- **Unscrapable**: Add to `.cursor/.dev/problem_lists/unscrapable.py` and continue with next problem

**CRITICAL**: Never edit generated files directly (helpers.py, test_solution.py, README.md, etc.). Always fix issues in the JSON template and regenerate to ensure reproducibility. The ONLY exception is solution.py implementation - you may edit this file directly to implement the optimal solution.

## Success Criteria

Each problem must meet:

- ✅ All files generated (README.md, solution.py, test_solution.py, helpers.py, playground.ipynb, **init**.py)
- ✅ **Optimal solution implemented** with correct algorithm
- ✅ **Multiple solution approaches** (e.g., Solution, SolutionOptimized)
- ✅ **Parametrized testing** for all solution approaches
- ✅ Linting passes without errors
- ✅ All tests pass
- ✅ **test-quality-assurance.md file read and complete workflow executed**
- ✅ Minimum 12 comprehensive test cases (verified via check_test_cases tool)
- ✅ **Test reproducibility verified** (tests pass consistently)
- ✅ Images included in README if available
- ✅ Proper JSON template created and updated
- ✅ Code coverage includes edge cases
- ✅ **Original solution preserved** after quality assurance process

## Batch Parameters

- **Count**: Number of problems to create (default: 5)
- **Tags**: Optional filter for specific problem lists
- **Force**: Whether to overwrite existing problems
- **Dry Run**: Preview mode without actual creation

## Unscrapable Problems Management

### Adding Unscrapable Problems

When encountering a problem that cannot be scraped (premium, API issues, etc.):

1. **Add to unscrapable list**: Update `.cursor/.dev/problem_lists/unscrapable.py`
2. **Format**: `(problem_number, "problem-name")`
3. **Continue batch**: The next_problem.py script will automatically skip unscrapable problems

### Example unscrapable.py entry:

```python
UNSCRAPABLE_PROBLEMS = [
    (252, "meeting-rooms"),
    (253, "meeting-rooms-ii"),  # if also unscrapable
    # Add more as discovered
]
```

## Notes

- **Sequential Processing**: Create one problem at a time to avoid conflicts
- **Progress Tracking**: Show clear progress indicators
- **Error Recovery**: Continue batch even if individual problems fail
- **Solution Implementation**: **MUST** implement optimal solution before quality assurance
- **Quality Focus**: Ensure each problem meets all quality standards
- **Reproducibility**: Verify tests pass consistently with implemented solutions
- **Documentation**: Maintain clear logs of the entire process
- **Unscrapable Handling**: Automatically exclude known unscrapable problems
