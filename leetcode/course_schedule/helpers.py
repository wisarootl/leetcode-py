def run_can_finish(solution_class: type, num_courses: int, prerequisites: list[list[int]]):
    implementation = solution_class()
    return implementation.can_finish(num_courses, prerequisites)


def assert_can_finish(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
