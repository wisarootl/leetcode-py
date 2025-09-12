def run_k_closest(solution_class: type, points: list[list[int]], k: int):
    implementation = solution_class()
    return implementation.k_closest(points, k)


def assert_k_closest(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
