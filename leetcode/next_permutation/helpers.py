def run_next_permutation(solution_class: type, nums: list[int]):
    implementation = solution_class()
    nums_copy = nums.copy()
    implementation.next_permutation(nums_copy)
    return nums_copy


def assert_next_permutation(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
