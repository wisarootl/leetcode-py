def run_top_k_frequent(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.top_k_frequent(nums, k)


def assert_top_k_frequent(result: list[int], expected: list[int]) -> bool:
    assert set(result) == set(expected)
    return True
