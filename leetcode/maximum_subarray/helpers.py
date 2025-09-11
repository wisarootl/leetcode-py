def run_max_sub_array(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_sub_array(nums)


def assert_max_sub_array(result: int, expected: int) -> bool:
    assert result == expected
    return True
