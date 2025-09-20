def run_top_k_frequent(solution_class: type, words: list[str], k: int):
    implementation = solution_class()
    return implementation.top_k_frequent(words, k)


def assert_top_k_frequent(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
