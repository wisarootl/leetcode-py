def run_two_sum(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.two_sum(nums, target)


def assert_two_sum(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
