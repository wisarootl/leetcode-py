def run_is_valid_sudoku(solution_class: type, board: list[list[str]]):
    implementation = solution_class()
    return implementation.is_valid_sudoku(board)


def assert_is_valid_sudoku(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
