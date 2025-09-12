from leetcode_py import ListNode


def run_merge_k_lists(solution_class: type, lists_data: list[list[int]]):
    lists = [ListNode[int].from_list(lst) for lst in lists_data]
    implementation = solution_class()
    return implementation.merge_k_lists(lists)


def assert_merge_k_lists(result: ListNode[int] | None, expected_data: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_data)
    assert result == expected
    return True
