from leetcode_py import ListNode


def run_reverse_between(solution_class: type, head_list: list[int], left: int, right: int):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.reverse_between(head, left, right)


def assert_reverse_between(result: ListNode[int] | None, expected_list: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_list)
    assert result == expected
    return True
