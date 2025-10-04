def run_longest_common_subsequence(solution_class: type, text1: str, text2: str):
    implementation = solution_class()
    return implementation.longest_common_subsequence(text1, text2)


def assert_longest_common_subsequence(result: int, expected: int) -> bool:
    assert result == expected
    return True
