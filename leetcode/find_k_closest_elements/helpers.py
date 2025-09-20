def run_find_closest_elements(solution_class: type, arr: list[int], k: int, x: int):
    implementation = solution_class()
    return implementation.find_closest_elements(arr, k, x)


def assert_find_closest_elements(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
