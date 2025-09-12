def run_oranges_rotting(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.oranges_rotting(grid)


def assert_oranges_rotting(result: int, expected: int) -> bool:
    assert result == expected
    return True
