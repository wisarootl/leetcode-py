from leetcode_py import ListNode


def run_reorder_list(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    implementation.reorder_list(head)
    return head.to_list() if head else []


def assert_reorder_list(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
