from leetcode_py import ListNode


def run_reverse_list(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.reverse_list(head)


def assert_reverse_list(result: ListNode[int] | None, expected_list: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_list)
    assert result == expected
    return True
