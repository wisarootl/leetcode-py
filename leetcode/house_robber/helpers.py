def run_rob(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.rob(nums)


def assert_rob(result: int, expected: int) -> bool:
    assert result == expected
    return True
