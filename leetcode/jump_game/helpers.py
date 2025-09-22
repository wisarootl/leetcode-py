def run_can_jump(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.can_jump(nums)


def assert_can_jump(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
