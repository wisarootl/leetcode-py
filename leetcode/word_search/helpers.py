def run_exist(solution_class: type, board: list[list[str]], word: str):
    implementation = solution_class()
    return implementation.exist(board, word)


def assert_exist(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
