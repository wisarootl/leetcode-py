# Migrate Problems to New Template Format

Migrate problems from `.templates/leetcode/json_old/` to `.templates/leetcode/json/` using the new template system.

## Migration Steps

1. **Find next**: `python .amazonq/plans/find_next_problem.py`
2. **Create JSON**: Analyze old format, create new template in `.templates/leetcode/json/`
3. **Generate**: `make p-gen PROBLEM=<name>`
4. **Lint**: `make p-lint PROBLEM=<name>` (fix JSON if fails, regenerate with `FORCE=1`)
5. **Implement**: Copy solution from `leetcode_old/`
6. **Test**: `make p-test PROBLEM=<name>`
7. **Enhance tests**: If only 2-3 cases, add edge cases (update JSON → regenerate → lint → test)
8. **Commit**: Save changes

## Progress

```bash
python .amazonq/plans/find_next_problem.py  # Next problem or "All problems updated!"
```
