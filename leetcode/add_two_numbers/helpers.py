from leetcode_py import ListNode


def run_add_two_numbers(solution_class: type, l1_vals: list[int], l2_vals: list[int]):
    l1 = ListNode.from_list(l1_vals)
    l2 = ListNode.from_list(l2_vals)
    implementation = solution_class()
    return implementation.add_two_numbers(l1, l2)


def assert_add_two_numbers(result: ListNode[int] | None, expected_vals: list[int]) -> bool:
    expected = ListNode.from_list(expected_vals)
    assert result == expected
    return True
