def run_count_substrings(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.count_substrings(s)


def assert_count_substrings(result: int, expected: int) -> bool:
    assert result == expected
    return True
