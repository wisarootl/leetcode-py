def run_min_window(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.min_window(s, t)


def assert_min_window(result: str, expected: str) -> bool:
    assert result == expected
    return True
