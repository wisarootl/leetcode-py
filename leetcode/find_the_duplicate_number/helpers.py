def run_find_duplicate(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_duplicate(nums)


def assert_find_duplicate(result: int, expected: int) -> bool:
    assert result == expected
    return True
