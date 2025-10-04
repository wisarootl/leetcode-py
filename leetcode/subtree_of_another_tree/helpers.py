from leetcode_py import TreeNode


def run_is_subtree(solution_class: type, root_list: list[int | None], sub_root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    sub_root = TreeNode[int].from_list(sub_root_list)
    implementation = solution_class()
    return implementation.isSubtree(root, sub_root)


def assert_is_subtree(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
