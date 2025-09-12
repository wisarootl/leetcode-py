from leetcode_py import ListNode


def run_merge_two_lists(solution_class: type, list1_vals: list[int], list2_vals: list[int]):
    list1 = ListNode[int].from_list(list1_vals)
    list2 = ListNode[int].from_list(list2_vals)
    implementation = solution_class()
    return implementation.merge_two_lists(list1, list2)


def assert_merge_two_lists(result: ListNode[int] | None, expected_vals: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_vals)
    assert result == expected
    return True
