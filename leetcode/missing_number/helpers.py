def run_missing_number(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.missing_number(nums)


def assert_missing_number(result: int, expected: int) -> bool:
    assert result == expected
    return True
