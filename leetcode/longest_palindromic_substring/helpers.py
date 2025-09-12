def run_longest_palindrome(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.longest_palindrome(s)


def assert_longest_palindrome(result: str, expected: set[str]) -> bool:
    assert result in expected
    return True
