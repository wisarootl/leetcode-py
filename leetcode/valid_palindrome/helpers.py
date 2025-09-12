def run_is_palindrome(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.is_palindrome(s)


def assert_is_palindrome(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
