def run_can_attend_meetings(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.can_attend_meetings(intervals)


def assert_can_attend_meetings(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
