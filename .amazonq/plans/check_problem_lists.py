# TODO: temporary use only while completing ongoing list

import json
import sys
from pathlib import Path

# Import the tuple lists
sys.path.append(str(Path(__file__).parent.parent.parent))
from algo_master_75_tuples import algo_master_75_tuples
from blind_75_tuples import blind_75_tuples
from neetcode_150_tuples import neetcode_150_tuples


def get_existing_problems():
    """Get problem numbers from existing JSON files."""
    json_dir = Path(__file__).parent.parent.parent / "leetcode_py/cli/resources/leetcode/json/problems"
    existing_problems = set()

    for json_file in json_dir.glob("*.json"):
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
                problem_number = int(data.get("problem_number", 0))
                if problem_number > 0:
                    existing_problems.add(problem_number)
        except (json.JSONDecodeError, ValueError, KeyError):
            continue

    return existing_problems


def check_problem_list(name, problem_tuples, existing_problems):
    """Check how many problems from a list are available."""
    problem_numbers = {num for num, _ in problem_tuples}
    have = problem_numbers & existing_problems
    missing = problem_numbers - existing_problems

    print(f"\n=== {name} ===")
    print(f"Total problems: {len(problem_numbers)}")
    print(f"Problems you have: {len(have)} ({len(have)/len(problem_numbers)*100:.1f}%)")
    print(f"Problems missing: {len(missing)} ({len(missing)/len(problem_numbers)*100:.1f}%)")

    if missing:
        print(f"Missing problems: {sorted(missing)}")

    return have, missing


def main():
    existing = get_existing_problems()
    print(f"Total existing problems in JSON: {len(existing)}")

    # Check each list
    blind_have, blind_missing = check_problem_list("BLIND 75", blind_75_tuples, existing)
    neetcode_have, neetcode_missing = check_problem_list("NEETCODE 150", neetcode_150_tuples, existing)
    algo_have, algo_missing = check_problem_list("ALGO MASTER 75", algo_master_75_tuples, existing)

    # Summary
    print("\n=== SUMMARY ===")
    print(f"Blind 75: {len(blind_have)}/75 ({len(blind_have)/75*100:.1f}%)")
    print(f"NeetCode 150: {len(neetcode_have)}/150 ({len(neetcode_have)/150*100:.1f}%)")
    print(f"Algo Master 75: {len(algo_have)}/75 ({len(algo_have)/75*100:.1f}%)")


if __name__ == "__main__":
    main()
