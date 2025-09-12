def run_update_matrix(solution_class: type, mat: list[list[int]]):
    implementation = solution_class()
    return implementation.update_matrix(mat)


def assert_update_matrix(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
