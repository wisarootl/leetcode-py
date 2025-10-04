def run_reverse_bits(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.reverse_bits(n)


def assert_reverse_bits(result: int, expected: int) -> bool:
    assert result == expected
    return True
