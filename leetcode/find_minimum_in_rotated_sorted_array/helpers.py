def run_find_min(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_min(nums)


def assert_find_min(result: int, expected: int) -> bool:
    assert result == expected
    return True
