def run_rotate(solution_class: type, matrix: list[list[int]]):
    import copy

    matrix_copy = copy.deepcopy(matrix)
    implementation = solution_class()
    implementation.rotate(matrix_copy)
    return matrix_copy


def assert_rotate(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
