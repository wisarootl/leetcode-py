def run_num_decodings(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.num_decodings(s)


def assert_num_decodings(result: int, expected: int) -> bool:
    assert result == expected
    return True
