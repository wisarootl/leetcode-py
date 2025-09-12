def run_merge(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.merge(intervals)


def assert_merge(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
