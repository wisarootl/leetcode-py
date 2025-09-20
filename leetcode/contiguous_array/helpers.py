def run_find_max_length(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.find_max_length(nums)


def assert_find_max_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
