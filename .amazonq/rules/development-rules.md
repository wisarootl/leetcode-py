# LeetCode Repository Rules

## Discussion Mode

- **Enter**: Prefix with "D:" for read-only analysis mode
- **Exit**: Use "XD:" to resume normal operations
- In discussion mode: NO code updates, only analysis/suggestions

## Code Standards

- Use snake_case for Python methods
- Include type hints: `list[str]`, `dict[str, int]`, `Type | None`
- Follow linting rules (black, isort, ruff, mypy)

## Testing

- Test specific: `make q-test QUESTION=<name>`
- Test all: `make test`
- Beautiful logging with loguru

## File Structure

Each problem has:

- `README.md` - Problem description
- `solution.py` - Implementation with TODO placeholder
- `tests.py` - Parametrized pytest tests
- `__init__.py` - Empty package file
