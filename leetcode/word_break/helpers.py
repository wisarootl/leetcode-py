def run_word_break(solution_class: type, s: str, word_dict: list[str]):
    implementation = solution_class()
    return implementation.word_break(s, word_dict)


def assert_word_break(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
