# Template Modification Rules

## Critical: Do NOT Modify Reference Directories

**NEVER modify these reference directories:**

- `.templates/leetcode/.example/` - Template reference examples
- `leetcode/.example/` - Generated file reference examples

These are reference implementations that show what the final generated files should look like.

## Only Modify Template Source

**ONLY modify the actual template directory:**

- `.templates/leetcode/{{cookiecutter.question_name}}/` - The actual cookiecutter template

## Workflow

1. **Modify**: Only `.templates/leetcode/{{cookiecutter.question_name}}/` files
2. **Generate**: `make q-gen QUESTION=name` → creates files in `leetcode/name/`
3. **Compare**: Generated `leetcode/name/` vs reference `leetcode/.example/name/`
4. **Validate**: `make q-validate QUESTION=name`

## Template Structure

```
.templates/leetcode/
├── {{cookiecutter.question_name}}/     ← MODIFY THESE FILES
│   ├── __init__.py
│   ├── solution.py
│   ├── tests.py
│   ├── README.md
│   └── playground.ipynb
├── cookiecutter.json                   ← MODIFY THIS CONFIG
└── gen.py                             ← MODIFY IF NEEDED
```

## Reference Structure (DO NOT MODIFY)

```
.templates/leetcode/.example/           ← DO NOT MODIFY
leetcode/.example/                      ← DO NOT MODIFY
```

This ensures template changes are properly tested against stable reference implementations.
