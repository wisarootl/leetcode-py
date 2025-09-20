from leetcode_py import ListNode


def run_odd_even_list(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    result = implementation.odd_even_list(head)
    return result.to_list() if result else []


def assert_odd_even_list(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
