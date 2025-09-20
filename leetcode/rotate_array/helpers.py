def run_rotate(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    nums_copy = nums[:]
    implementation.rotate(nums_copy, k)
    return nums_copy


def assert_rotate(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
