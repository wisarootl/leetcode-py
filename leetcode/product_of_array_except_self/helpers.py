def run_product_except_self(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.product_except_self(nums)


def assert_product_except_self(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
