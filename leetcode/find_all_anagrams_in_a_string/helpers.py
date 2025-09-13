def run_find_anagrams(solution_class: type, s: str, p: str):
    implementation = solution_class()
    return implementation.find_anagrams(s, p)


def assert_find_anagrams(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
