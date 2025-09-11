from leetcode_py import TreeNode


def run_lowest_common_ancestor(
    solution_class: type, root_list: list[int | None], p_val: int, q_val: int
):
    root = TreeNode[int].from_list(root_list)
    assert root is not None
    p = root.find_node(p_val)
    q = root.find_node(q_val)
    assert p is not None and q is not None
    implementation = solution_class()
    return implementation.lowest_common_ancestor(root, p, q)


def assert_lowest_common_ancestor(result: TreeNode[int] | None, expected_val: int) -> bool:
    assert result is not None
    assert result.val == expected_val
    return True
