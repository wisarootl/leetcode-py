# TODO: temporary use only while completing ongoing list

import sys
from pathlib import Path

# Import the problem lists
sys.path.append(str(Path(__file__).parent.parent.parent))
from problem_lists import available_lists
from problem_lists.unscrapable import get_unscrapable_numbers
from problem_lists.utils import get_existing_problems


def get_next_problem(tag_names=None):
    """Get the next problem to work on from the list with the lowest missing problems."""
    if tag_names is None:
        tag_names = list(available_lists.keys())

    existing_problems = get_existing_problems()
    unscrapable_numbers = get_unscrapable_numbers()

    # Find the list with the lowest missing problems
    best_list = None
    min_missing = float("inf")
    missing_problems = []

    for tag_name, problem_tuples in available_lists.items():
        if tag_name in tag_names:
            problem_numbers = {num for num, _ in problem_tuples}
            # Exclude unscrapable problems from missing problems
            missing = problem_numbers - existing_problems - unscrapable_numbers
            missing_count = len(missing)

            if missing_count > 0 and missing_count < min_missing:
                min_missing = missing_count
                best_list = tag_name
                missing_problems = sorted(missing)

    if not missing_problems:
        print("No missing problems found in any of the specified lists!")
        return None

    # Get the first missing problem from the best list
    next_problem_number = missing_problems[0]

    # Find the problem name
    problem_tuples = available_lists[best_list]
    problem_name = None
    for num, name in problem_tuples:
        if num == next_problem_number:
            problem_name = name
            break

    result = {
        "tag_name": best_list,
        "problem_number": next_problem_number,
        "problem_name": problem_name,
        "missing_count": min_missing,
        "total_in_list": len(available_lists[best_list]),
    }

    return result


def main():
    next_problem = get_next_problem()
    if next_problem:
        completed = next_problem["total_in_list"] - next_problem["missing_count"]
        total = next_problem["total_in_list"]
        percentage = completed / total * 100

        print("\n🎯 Next problem to work on:")
        print(f"   Problem #{next_problem['problem_number']} - {next_problem['problem_name']}")
        print(f"   Tag: {next_problem['tag_name']}")
        print(f"   Progress: {completed}/{total} ({percentage:.1f}%)")


if __name__ == "__main__":
    main()
