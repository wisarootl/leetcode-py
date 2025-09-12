def run_spiral_order(solution_class: type, matrix: list[list[int]]):
    implementation = solution_class()
    return implementation.spiral_order(matrix)


def assert_spiral_order(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
