def run_num_islands(solution_class: type, grid: list[list[str]]):
    implementation = solution_class()
    return implementation.num_islands(grid)


def assert_num_islands(result: int, expected: int) -> bool:
    assert result == expected
    return True
