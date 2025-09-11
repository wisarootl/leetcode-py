def run_length_of_longest_substring(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.length_of_longest_substring(s)


def assert_length_of_longest_substring(result: int, expected: int) -> bool:
    assert result == expected
    return True
