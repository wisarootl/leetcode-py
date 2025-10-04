# Update Tags Command

## Description

Updates `.tags.json5` by running the `update_tags.py` script, sorting the output alphabetically, and cleaning up temporary files. The LLM handles this process directly to preserve comments in the JSON5 file.

## Usage

When user requests "update tags" or "update-tags", the assistant will:

1. **Run update script**: Execute `poetry run python .cursor/.dev/update_tags.py`
2. **Read output**: Read the generated `.cursor/.dev/update_tags.json` file
3. **Read current tags**: Read the existing `.tags.json5` file to preserve comments
4. **Sort and merge**: Sort the new tags alphabetically by name and merge with existing structure
5. **Update file**: Write the updated tags to `.tags.json5` while preserving comments
6. **Cleanup**: Delete the temporary `.cursor/.dev/update_tags.json` file

## LLM Workflow

```python
# 1. Run the update script
poetry run python .cursor/.dev/update_tags.py

# 2. Read the generated JSON file
with open('.cursor/.dev/update_tags.json', 'r') as f:
    new_tags = json.load(f)

# 3. Read existing .tags.json5 to preserve comments
with open('.tags.json5', 'r') as f:
    existing_content = f.read()

# 4. Sort new tags alphabetically by name
sorted_tags = sorted(new_tags, key=lambda x: x.get('name', ''))

# 5. Update the .tags.json5 file while preserving comments
# (Implementation depends on JSON5 structure and comment preservation needs)

# 6. Clean up temporary file
os.remove('.cursor/.dev/update_tags.json')
```

## Prerequisites

- `update_tags.py` script must exist in `.cursor/.dev/`
- The script must output a JSON file to `.cursor/.dev/update_tags.json`
- Assistant must handle JSON5 comment preservation

## Output

- Updates `.tags.json5` with alphabetically sorted tags
- Preserves existing comments in the JSON5 file
- Removes temporary `.cursor/.dev/update_tags.json` file
- Provides success/error feedback
