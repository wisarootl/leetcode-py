def run_largest_rectangle_area(solution_class: type, heights: list[int]):
    implementation = solution_class()
    return implementation.largest_rectangle_area(heights)


def assert_largest_rectangle_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
