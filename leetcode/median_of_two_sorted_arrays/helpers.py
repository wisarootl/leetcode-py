def run_find_median_sorted_arrays(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.find_median_sorted_arrays(nums1, nums2)


def assert_find_median_sorted_arrays(result: float, expected: float) -> bool:
    assert abs(result - expected) < 1e-5
    return True
