def run_erase_overlap_intervals(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.erase_overlap_intervals(intervals)


def assert_erase_overlap_intervals(result: int, expected: int) -> bool:
    assert result == expected
    return True
