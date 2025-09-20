def run_decode_string(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.decode_string(s)


def assert_decode_string(result: str, expected: str) -> bool:
    assert result == expected
    return True
