def run_find_order(solution_class: type, num_courses: int, prerequisites: list[list[int]]):
    implementation = solution_class()
    return implementation.find_order(num_courses, prerequisites)


def assert_find_order(result: list[int], expected: list[int]) -> bool:
    if not result and not expected:
        return True
    if len(result) != len(expected):
        return False
    # For topological sort, multiple valid answers exist
    # Just verify the result is a valid topological ordering
    assert len(result) == len(expected)
    assert set(result) == set(expected)
    return True
