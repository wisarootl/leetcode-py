def run_combination_sum(solution_class: type, candidates: list[int], target: int):
    implementation = solution_class()
    return implementation.combination_sum(candidates, target)


def assert_combination_sum(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for comparison
    result_sorted = [sorted(combo) for combo in result]
    expected_sorted = [sorted(combo) for combo in expected]
    result_sorted.sort()
    expected_sorted.sort()
    assert result_sorted == expected_sorted
    return True
