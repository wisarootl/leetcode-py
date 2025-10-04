def run_count_bits(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_bits(n)


def assert_count_bits(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
