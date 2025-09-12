def run_ladder_length(solution_class: type, begin_word: str, end_word: str, word_list: list[str]):
    implementation = solution_class()
    return implementation.ladder_length(begin_word, end_word, word_list)


def assert_ladder_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
