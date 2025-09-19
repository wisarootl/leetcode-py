def run_max_product(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_product(nums)


def assert_max_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
