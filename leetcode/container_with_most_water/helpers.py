def run_max_area(solution_class: type, height: list[int]):
    implementation = solution_class()
    return implementation.max_area(height)


def assert_max_area(result: int, expected: int) -> bool:
    assert result == expected
    return True
