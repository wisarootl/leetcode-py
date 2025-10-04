# TODO: temporary use only while completing ongoing list

import json
import sys
from pathlib import Path

# Import the problem lists and resources
sys.path.append(str(Path(__file__).parent.parent.parent))
from problem_lists import available_lists

from leetcode_py.cli.utils.problem_finder import find_problems_by_tag


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


def update_tags(tag_names=None):
    """Update tags.json5 format for the specified tag names, comparing with existing tags."""
    if tag_names is None:
        tag_names = list(available_lists.keys())

    existing_problems = get_existing_problems()

    # Generate update tags content with only missing problems
    update_tags = {}
    changes_found = False

    for tag_name, problem_tuples in available_lists.items():
        if tag_name in tag_names:
            # Get new problems from our problem lists
            new_problem_names = set(get_tag_problems(problem_tuples, existing_problems))

            # Get existing problems using the recursive tag resolution
            existing_problem_names = set(find_problems_by_tag(tag_name))

            # Only include missing problems (added, not removed)
            missing_problems = new_problem_names - existing_problem_names
            removed_problems = existing_problem_names - new_problem_names

            if missing_problems or removed_problems:
                changes_found = True

                # Only include missing problems in the update
                if missing_problems:
                    update_tags[tag_name] = sorted(missing_problems)
                    print(
                        f"{tag_name}: Missing {len(missing_problems)} problems: {sorted(missing_problems)}"
                    )

                if removed_problems:
                    print(
                        f"{tag_name}: Removed {len(removed_problems)} problems: {sorted(removed_problems)} (not included in update)"
                    )

    if not changes_found:
        print("No changes found in any of the specified tags.")
        return

    # Generate update_tags.json content with only missing problems
    output_file = Path(__file__).parent / "update_tags.json"
    with open(output_file, "w") as f:
        json.dump(update_tags, f, indent=4)

    print(f"\nUpdate tags with missing problems written to {output_file}")
    print(f"Total tags with missing problems: {len(update_tags)}")


if __name__ == "__main__":
    # Update all available lists by default
    update_tags()
