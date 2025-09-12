def run_insert(solution_class: type, intervals: list[list[int]], new_interval: list[int]):
    implementation = solution_class()
    return implementation.insert(intervals, new_interval)


def assert_insert(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
