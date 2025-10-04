def run_character_replacement(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.character_replacement(s, k)


def assert_character_replacement(result: int, expected: int) -> bool:
    assert result == expected
    return True
