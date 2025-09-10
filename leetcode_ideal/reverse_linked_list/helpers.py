from leetcode_py import ListNode


def create_list(head_list: list[int]) -> ListNode[int] | None:
    return ListNode.from_list(list(head_list))


def run_reverse_list(solution_class: type, head_list: list[int]) -> ListNode[int] | None:
    head = create_list(head_list)
    return solution_class().reverse_list(head)


def assert_reverse_list(result: ListNode[int] | None, expected: ListNode[int] | None) -> bool:
    assert result == expected
    return True
