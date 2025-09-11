# Migrate Problems to New Template Format

Migrate problems from `.templates/leetcode/json_old/` to `.templates/leetcode/json/` using the new template system.

## Migration Steps

1. **Create JSON**: Analyze old format, create new template in `.templates/leetcode/json/` (reference `.templates/leetcode/examples/` for format)
2. **Generate**: `make p-gen PROBLEM=<name>`
3. **Lint**: `make p-lint PROBLEM=<name>` (fix JSON if fails, regenerate with `FORCE=1`)
4. **Implement**: Look at `leetcode_old/` code - copy solution with all comments/notes and review test cases
    - **Important**: Re-copy solution after `p-gen` since it overwrites with TODO placeholders
    - **Multiple solutions**: If old code has alternative implementations (e.g., Solution, SolutionDFS, SolutionBFS),
      add parametrize to test all classes (see lru_cache as example)
5. **Test**: `make p-test PROBLEM=<name>`
6. **Enhance tests**: Review test coverage - check if cases cover edge scenarios:
    - Boundary values (min/max constraints, empty inputs)
    - Different input sizes/lengths
    - Zero/null cases, single elements
    - Error conditions, special values
    - If only 2-3 basic cases, add comprehensive edge cases (update JSON → regenerate with `FORCE=1` → lint → re-copy solution → test)

## Progress

```bash
python .amazonq/plans/find_next_problem.py  # Next problem or "All problems updated!"
```
