def run_three_sum(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.three_sum(nums)


def assert_three_sum(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = [sorted(triplet) for triplet in result]
    expected_sorted = [sorted(triplet) for triplet in expected]
    result_sorted.sort()
    expected_sorted.sort()
    assert result_sorted == expected_sorted
    return True
