def run_min_meeting_rooms(solution_class: type, intervals: list[list[int]]):
    implementation = solution_class()
    return implementation.min_meeting_rooms(intervals)


def assert_min_meeting_rooms(result: int, expected: int) -> bool:
    assert result == expected
    return True
