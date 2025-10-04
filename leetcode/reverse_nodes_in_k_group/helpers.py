from leetcode_py import ListNode


def run_reverse_k_group(solution_class: type, head_vals: list[int], k: int):
    head = ListNode.from_list(head_vals)
    implementation = solution_class()
    return implementation.reverse_k_group(head, k)


def assert_reverse_k_group(result: ListNode[int] | None, expected_vals: list[int]) -> bool:
    expected = ListNode.from_list(expected_vals)
    assert result == expected
    return True
