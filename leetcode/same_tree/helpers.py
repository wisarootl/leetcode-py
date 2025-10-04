from leetcode_py import TreeNode


def run_is_same_tree(solution_class: type, p_list: list[int | None], q_list: list[int | None]):
    p = TreeNode[int].from_list(p_list)
    q = TreeNode[int].from_list(q_list)
    implementation = solution_class()
    return implementation.is_same_tree(p, q)


def assert_is_same_tree(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
