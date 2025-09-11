# Migrate Problems to New Template Format

Migrate problems from `.templates/leetcode/json_old/` to `.templates/leetcode/json/` using the new template system.

## Migration Steps

**Note**: Commands require UI confirmation popup - click "Run" when prompted for `make` commands.

1. **Create JSON**: Analyze old format, create new template in `.templates/leetcode/json/` (reference `.templates/leetcode/examples/` for format)
2. **Generate**: `make p-gen PROBLEM=<name>`
3. **Lint**: `make p-lint PROBLEM=<name>` (fix JSON if fails, regenerate with `FORCE=1`)
4. **Enhance tests**: Review test coverage - check if cases cover edge scenarios:
    - **Check old tests**: Examine `leetcode_old/<problem>/tests.py` for comprehensive test coverage
    - **Update JSON**: Add relevant/generalizable test cases to JSON template (exclude problem-specific error handling)
    - Boundary values (min/max constraints, empty inputs)
    - Different input sizes/lengths
    - Zero/null cases, single elements
    - Error conditions, special values
    - If only 2-3 basic cases, add comprehensive edge cases (update JSON → regenerate with `FORCE=1` → lint → re-copy solution → test)
5. **Implement**: Look at `leetcode_old/` code - copy solution with all comments/notes
    - **Important**: Re-copy solution after `p-gen` since it overwrites with TODO placeholders
    - **Multiple solutions**: If old code has alternative implementations (e.g., Solution, SolutionDFS, SolutionBFS),
      add parametrize to test all classes (see lru_cache as example)
6. **Test**: `make p-test PROBLEM=<name>` (edit JSON and revalidate for reproducibility if needed)

## Progress

```bash
python .amazonq/plans/find_next_problem.py  # Next problem or "All problems updated!"
```
