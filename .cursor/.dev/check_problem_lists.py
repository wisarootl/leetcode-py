# TODO: temporary use only while completing ongoing list

import sys
from pathlib import Path

# Import the problem lists
sys.path.append(str(Path(__file__).parent.parent.parent))
from problem_lists import available_lists
from problem_lists.utils import get_existing_problems


def check_problem_list(tag_name, problem_tuples, existing_problems):
    """Check how many problems from a list are available."""
    problem_numbers = {num for num, _ in problem_tuples}
    have = problem_numbers & existing_problems
    missing = problem_numbers - existing_problems

    print(f"\n=== {tag_name.upper()} ===")
    print(f"Total problems: {len(problem_numbers)}")
    print(f"Problems you have: {len(have)} ({len(have)/len(problem_numbers)*100:.1f}%)")
    print(f"Problems missing: {len(missing)} ({len(missing)/len(problem_numbers)*100:.1f}%)")

    if missing:
        print(f"Missing problems: {sorted(missing)}")

    return have, missing


def check_problem_lists(tag_names=None):
    """Check problem lists for available problems."""
    if tag_names is None:
        tag_names = list(available_lists.keys())

    existing = get_existing_problems()
    print(f"Total existing problems in JSON: {len(existing)}")

    results = {}

    # Check each specified list
    for tag_name, problem_tuples in available_lists.items():
        if tag_name in tag_names:
            have, missing = check_problem_list(tag_name, problem_tuples, existing)
            results[tag_name] = {"have": have, "missing": missing, "total": len(problem_tuples)}

    # Summary
    print("\n=== SUMMARY ===")
    for tag_name, result in results.items():
        total = result["total"]
        have_count = len(result["have"])
        percentage = have_count / total * 100
        print(f"{tag_name}: {have_count}/{total} ({percentage:.1f}%)")

    return results


def main():
    check_problem_lists()


if __name__ == "__main__":
    main()
