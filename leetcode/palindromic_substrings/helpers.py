def run_count_substrings(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.countSubstrings(s)


def assert_count_substrings(result: int, expected: int) -> bool:
    assert result == expected
    return True
