def run_find_words(solution_class: type, board: list[list[str]], words: list[str]):
    implementation = solution_class()
    return implementation.find_words(board, words)


def assert_find_words(result: list[str], expected: list[str]) -> bool:
    assert set(result) == set(expected)
    return True
