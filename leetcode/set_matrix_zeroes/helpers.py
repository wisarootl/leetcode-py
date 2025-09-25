def run_set_zeroes(solution_class: type, matrix: list[list[int]]):
    import copy

    matrix_copy = copy.deepcopy(matrix)
    implementation = solution_class()
    implementation.set_zeroes(matrix_copy)
    return matrix_copy


def assert_set_zeroes(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
