def run_pacific_atlantic(solution_class: type, heights: list[list[int]]):
    implementation = solution_class()
    return implementation.pacific_atlantic(heights)


def assert_pacific_atlantic(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
