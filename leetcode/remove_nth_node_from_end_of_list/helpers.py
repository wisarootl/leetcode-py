from leetcode_py import ListNode


def run_remove_nth_from_end(solution_class: type, head_list: list[int], n: int):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    result = implementation.remove_nth_from_end(head, n)
    return result.to_list() if result else []


def assert_remove_nth_from_end(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
