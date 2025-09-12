# Test Case Enhancement Automation Scripts

This directory contains prebuilt scripts to streamline the test case enhancement process for LeetCode problems.

## Scripts Overview

### 🔍 `find_problems_needing_enhancement.sh`

**Purpose**: Find problems with insufficient test cases
**Usage**: `bash find_problems_needing_enhancement.sh [threshold] [max_results]`
**Example**: `bash find_problems_needing_enhancement.sh 10 5`

### 🚀 `enhance_single_problem.sh`

**Purpose**: Enhance test cases for a single problem (full automated workflow)
**Usage**: `bash enhance_single_problem.sh <problem_name>`
**Example**: `bash enhance_single_problem.sh two_sum`

### 📦 `enhance_batch_problems.sh`

**Purpose**: Enhance test cases for multiple problems in batch
**Usage**: `bash enhance_batch_problems.sh [max_problems] [threshold]`
**Example**: `bash enhance_batch_problems.sh 5 10`

### ✅ `verify_enhancement.sh`

**Purpose**: Verify that test case enhancement was successful
**Usage**: `bash verify_enhancement.sh <problem_name>`
**Example**: `bash verify_enhancement.sh two_sum`

## Typical Workflow

1. **Find problems needing enhancement**:

    ```bash
    bash .amazonq/rules/test-case-enhancement/scripts/find_problems_needing_enhancement.sh
    ```

2. **Enhance problems** (choose one):

    ```bash
    # Single problem
    bash .amazonq/rules/test-case-enhancement/scripts/enhance_single_problem.sh <problem_name>

    # Batch enhancement
    bash .amazonq/rules/test-case-enhancement/scripts/enhance_batch_problems.sh
    ```

3. **Verify results**:
    ```bash
    bash .amazonq/rules/test-case-enhancement/scripts/verify_enhancement.sh <problem_name>
    ```

## What the Scripts Do

### Automated Process

1. **Backup** original problem structure
2. **Regenerate** from enhanced JSON templates
3. **Lint check** to ensure code quality
4. **Preserve** enhanced test files
5. **Restore** original solution code
6. **Verify** final state

### Safety Features

- Automatic backups before any changes
- Rollback capability if errors occur
- Syntax validation of generated tests
- Comprehensive error handling

## Requirements

- All scripts must be run from the repository root directory
- Requires `poetry`, `make`, and standard Unix tools
- JSON templates must be updated with enhanced test cases before running scripts
