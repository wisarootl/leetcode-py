# LeetCode Repository Rules

## Discussion Mode

- **Discussion Mode**: Prefix prompt with "D:" to enter read-only discussion mode
- In discussion mode: NO code updates, only read files and provide analysis/suggestions
- Always start responses with "[Discussion Mode]" header when in discussion mode
- Never exit discussion mode automatically - only when user uses "XD:" prefix
- If user seems to want code changes, remind them to use "XD:" to exit discussion mode
- **Exit Discussion**: Use "XD:" prefix to exit discussion mode and resume normal operations

## Code Standards

- Use snake_case for Python method names (following Python convention)
- Always include type hints for function parameters and return types
- Use PEP 585/604 syntax: `list[str]`, `dict[str, int]`, `Type | None`, etc.
- Add return statements to satisfy type checkers even if unreachable
- Follow the project's linting rules (black, isort, ruff, mypy)

## Template Usage

- **When user copies LeetCode problem**: Use `leetcode/_template/` to structure the question
- Copy template files to new question directory: `leetcode/{question_name}/`
- Replace template placeholders with actual problem details:
    - `{method_name}` - snake_case method name (e.g., `two_sum`)
    - `{ClassName}` - PascalCase class name (e.g., `TwoSum`)
    - `{parameters}` - method parameters with types
    - `{return_type}` - return type annotation
    - Test case placeholders with actual examples
- **Template Implementation**: Do NOT implement the Solution class - only provide test cases and structure
- **Helper Functions/Classes**: If the question relies on underlying helper functions or classes (e.g., TreeNode, ListNode):
    - First check if implementation already exists in `leetcode_py/common/` directory
    - If found, import from common module
    - If not found, create shared implementation in `leetcode_py/common/` for reusable classes
    - For question-specific helpers, implement directly in the solution file
- **Update Makefile**: When adding new question, update the default `QUESTION` value in Makefile to the new question name
- Always use the template structure for consistency

## File Structure

Each LeetCode problem should have:

- `README.md` - Problem description and examples
- `solution.py` - Solution implementation
- `tests.py` - Parametrized pytest tests with loguru logging
- `__init__.py` - Empty file for Python package

## Testing

- Use `make test-question QUESTION=<question_name>` to run tests
- Use `make test` to run all questions with coverage
- Default question is set to `two_sum` in Makefile
- Tests should cover all provided examples
- Use loguru for beautiful logging in tests
