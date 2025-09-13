def run_find_diagonal_order(solution_class: type, mat: list[list[int]]):
    implementation = solution_class()
    return implementation.find_diagonal_order(mat)


def assert_find_diagonal_order(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
