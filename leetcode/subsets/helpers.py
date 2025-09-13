def run_subsets(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.subsets(nums)


def assert_subsets(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = [sorted(subset) for subset in sorted(result)]
    expected_sorted = [sorted(subset) for subset in sorted(expected)]
    assert result_sorted == expected_sorted
    return True
