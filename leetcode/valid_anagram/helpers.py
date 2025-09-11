def run_is_anagram(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.is_anagram(s, t)


def assert_is_anagram(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
