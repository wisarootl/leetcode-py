def run_sort_colors(solution_class: type, nums: list[int]):
    nums_copy = nums.copy()
    implementation = solution_class()
    implementation.sort_colors(nums_copy)
    return nums_copy


def assert_sort_colors(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
