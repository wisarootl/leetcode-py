def run_contains_duplicate(solution_class: type, nums: list[int]) -> bool:
    return solution_class().contains_duplicate(nums)


def assert_contains_duplicate(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
