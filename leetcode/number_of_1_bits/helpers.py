def run_hamming_weight(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.hammingWeight(n)


def assert_hamming_weight(result: int, expected: int) -> bool:
    assert result == expected
    return True
