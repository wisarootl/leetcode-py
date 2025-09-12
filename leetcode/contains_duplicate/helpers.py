def run_contains_duplicate(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.contains_duplicate(nums)


def assert_contains_duplicate(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
