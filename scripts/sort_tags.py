#!/usr/bin/env python3
import sys

import json5

tags_file = "leetcode_py/cli/resources/leetcode/json/tags.json5"

with open(tags_file) as f:
    data = json5.load(f)

unsorted_tags = []
for tag_name, problems in data.items():
    if isinstance(problems, list):
        dicts = [item for item in problems if isinstance(item, dict)]
        strings = [item for item in problems if isinstance(item, str)]
        expected_order = dicts + sorted(strings)

        if problems != expected_order:
            unsorted_tags.append((tag_name, problems, expected_order))

if unsorted_tags:
    print("❌ Found unsorted problem lists:")
    for tag_name, current, expected in unsorted_tags:
        print(f"\n{tag_name}:")
        print(f"  Expected: {expected}")
    sys.exit(1)
else:
    print("✅ All problem lists are sorted!")
    sys.exit(0)
