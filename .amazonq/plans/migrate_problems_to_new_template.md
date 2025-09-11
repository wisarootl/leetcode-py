# Migrate Problems to New Template Format

Migrate problems from `.templates/leetcode/json_old/` to `.templates/leetcode/json/` using the new template system.

## Migration Steps

1. **Create JSON**: Analyze old format, create new template in `.templates/leetcode/json/`
2. **Generate**: `make p-gen PROBLEM=<name>`
3. **Lint**: `make p-lint PROBLEM=<name>` (fix JSON if fails, regenerate with `FORCE=1`)
4. **Implement**: Look at `leetcode_old/` code - copy solution with all comments/notes and review test cases
    - **Important**: Re-copy solution after `p-gen` since it overwrites with TODO placeholders
    - **Multiple solutions**: If old code has alternative implementations (e.g., Solution, SolutionDFS, SolutionBFS),
      add parametrize to test all classes (see lru_cache as example)
5. **Test**: `make p-test PROBLEM=<name>`
6. **Enhance tests**: If only 2-3 cases, add edge cases (update JSON → regenerate → lint → test)

## Progress

```bash
python .amazonq/plans/find_next_problem.py  # Next problem or "All problems updated!"
```
