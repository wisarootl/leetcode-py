def run_can_partition(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.can_partition(nums)


def assert_can_partition(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
