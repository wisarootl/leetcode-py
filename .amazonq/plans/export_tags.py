# TODO: temporary use only while completing ongoing list

import json
import sys
from pathlib import Path

# Import the tuple lists
sys.path.append(str(Path(__file__).parent.parent.parent))
from algo_master_75_tuples import algo_master_75_tuples
from neetcode_150_tuples import neetcode_150_tuples


def get_existing_problems():
    """Get problem numbers and names from existing JSON files."""
    json_dir = Path(__file__).parent.parent.parent / "leetcode_py/cli/resources/leetcode/json/problems"
    existing_problems = {}

    for json_file in json_dir.glob("*.json"):
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
                problem_number = int(data.get("problem_number", 0))
                if problem_number > 0:
                    existing_problems[problem_number] = json_file.stem
        except (json.JSONDecodeError, ValueError, KeyError):
            continue

    return existing_problems


def get_tag_problems(problem_tuples, existing_problems):
    """Get problem names for existing problems from a tuple list."""
    problem_names = []
    for num, _ in problem_tuples:
        if num in existing_problems:
            problem_names.append(existing_problems[num])
    return sorted(problem_names)


def export_tags():
    """Export tags.json5 format for the three problem lists."""
    existing = get_existing_problems()

    # Get problem names for each list
    neetcode_150_names = get_tag_problems(neetcode_150_tuples, existing)
    algo_master_75_names = get_tag_problems(algo_master_75_tuples, existing)

    # Generate tags.json5 content
    content = """{\n"""

    # NeetCode 150
    content += f"    // NeetCode 150 - {len(neetcode_150_names)} problems\n"
    content += '    "neetcode-150": [\n'
    for name in neetcode_150_names:
        content += f'        "{name}",\n'
    content += "    ],\n\n"

    # Algo Master 75
    content += f"    // Algo Master 75 - {len(algo_master_75_names)} problems\n"
    content += '    "algo-master-75": [\n'
    for name in algo_master_75_names:
        content += f'        "{name}",\n'
    content += "    ],\n\n"

    # Test tag
    content += "    // Test tag for development and testing\n"
    content += '    test: ["binary_search", "two_sum", "valid_palindrome"],\n'
    content += "}\n"

    # Write to file
    output_file = Path(__file__).parent / "new_tags.json5"
    with open(output_file, "w") as f:
        f.write(content)

    print(f"Exported tags to {output_file}")
    print(f"NeetCode 150: {len(neetcode_150_names)} problems")
    print(f"Algo Master 75: {len(algo_master_75_names)} problems")


if __name__ == "__main__":
    export_tags()
