# LLM-Assisted Problem Creation Guide

This guide demonstrates how to leverage Large Language Models (LLMs) like Amazon Q, GitHub Copilot Chat, or Cursor to automatically generate new LeetCode problems for your practice environment.

## Overview

The LLM-assisted workflow enables you to add new problems to your collection with a simple natural language command. The AI assistant handles the entire process from scraping problem data to generating the complete problem structure with comprehensive test cases.

## Prerequisites

### Required LLM Context

For optimal results, include these rule files in your LLM context:

- [`.amazonq/rules/problem-creation.md`](../.amazonq/rules/problem-creation.md) - Complete problem generation workflow
- [`.amazonq/rules/test-quality-assurance.md`](../.amazonq/rules/test-quality-assurance.md) - Test enhancement and reproducibility verification
- [`.amazonq/rules/development-rules.md`](../.amazonq/rules/development-rules.md) - Code standards and testing patterns

### Setup Your IDE

Configure your IDE with an LLM assistant:

- **Amazon Q**: Install the Amazon Q plugin
- **GitHub Copilot**: Enable Copilot Chat
- **Cursor**: Built-in AI assistant
- **Other**: Any IDE with LLM integration

## Quick Start

### Basic Problem Addition

Simply ask your LLM assistant to add a problem:

![Prompt with Context](https://raw.githubusercontent.com/wisarootl/leetcode-py/main/docs/images/prompt-with-context.png)

_Example prompt showing how to request a new problem with the LLM assistant_

```bash
# Simple commands that work:
"Add problem 198. House Robber"
"Add problem 198. House Robber. tag: grind"
"Create problem 70. Climbing Stairs with grind-75 tag"
```

### What Happens Automatically

The LLM assistant will execute the complete workflow:

1. **Scrape** problem data from LeetCode
2. **Transform** data into proper JSON template format (including images)
3. **Create** JSON file in `leetcode_py/cli/resources/leetcode/json/problems/{problem_name}.json`
4. **Update** `leetcode_py/cli/resources/leetcode/json/tags.json5` with specified tags
5. **Generate** complete problem structure in `leetcode/{problem_name}/`
6. **Verify** with linting checks (iterates from step 3 until all pass)

![Problems Are Generated](https://raw.githubusercontent.com/wisarootl/leetcode-py/main/docs/images/problems-are-generated.png)

_Source control view showing all files created and modified during the problem generation process_

## Generated Problem Structure

### Solution Template

The assistant generates a clean solution template with proper type hints:

![Generated Solution](https://raw.githubusercontent.com/wisarootl/leetcode-py/main/docs/images/generated-solution.png)

_Generated solution.py file with TODO placeholder and proper method signature_

### Comprehensive Test Suite

Each problem includes 10+ test cases covering edge cases (note: generated test cases may need verification for correctness):

![Generated Test](https://raw.githubusercontent.com/wisarootl/leetcode-py/main/docs/images/generated-test.png)

_Generated test_solution.py with parametrized tests and comprehensive test cases_

## Test Enhancement Workflow

### Enhancing Existing Problems

Improve test coverage for existing problems:

```bash
"Enhance test cases for two_sum problem"
"Add more edge cases to binary_tree_inorder_traversal"
"Fix test reproducibility for valid_palindrome"
```

### Quality Assurance

The assistant can identify problems needing more test cases and verify test case correctness and reproducibility:

```bash
"Check which problems need more test cases"
"Find problems with less than 12 test cases"
"Verify test case correctness for house_robber"
"Fix test reproducibility for binary_tree_inorder_traversal"
```

## Best Practices

### Effective Prompts

**Good prompts:**

- "Add problem 198. House Robber with grind tag"
- "Create problem 70. Climbing Stairs for grind-75"
- "Enhance test cases for two_sum problem"

**Avoid:**

- Vague requests without problem numbers
- Requests for non-existent problems

## Troubleshooting

### Common Issues

**Template errors:**

- Assistant will automatically fix JSON template issues
- Re-runs generation until linting passes
- If JSON template fails after many iterations, ask agent to review the example template carefully as mentioned in the rules

**Test failures:**

- Assistant verifies test cases against expected outputs
- Fixes incorrect expected values
- Use test QA workflow for comprehensive test enhancement and reproducibility verification

## Integration with Development Workflow

### CI/CD Compatibility

Generated problems integrate seamlessly with:

- **Test Reproducibility** - CI automatically verifies problems can be regenerated consistently; just implement your solution and CI handles the rest

## Conclusion

LLM-assisted problem creation transforms the tedious process of adding new problems into a simple natural language interaction. The assistant handles all the complexity while ensuring professional code quality and comprehensive test coverage.

Start practicing with your new problems immediately - the assistant takes care of everything else!
