from leetcode_py import ListNode


def run_swap_pairs(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    result = implementation.swap_pairs(head)
    return result.to_list() if result else []


def assert_swap_pairs(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
