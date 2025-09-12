def run_permute(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.permute(nums)


def assert_permute(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = [sorted(perm) for perm in result]
    expected_sorted = [sorted(perm) for perm in expected]
    result_sorted.sort()
    expected_sorted.sort()
    assert len(result) == len(expected)
    assert result_sorted == expected_sorted
    return True
