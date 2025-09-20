def run_longest_consecutive(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.longest_consecutive(nums)


def assert_longest_consecutive(result: int, expected: int) -> bool:
    assert result == expected
    return True
