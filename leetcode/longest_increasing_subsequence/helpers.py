def run_length_of_lis(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.length_of_lis(nums)


def assert_length_of_lis(result: int, expected: int) -> bool:
    assert result == expected
    return True
