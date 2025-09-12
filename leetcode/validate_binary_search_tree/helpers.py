from leetcode_py import TreeNode


def run_is_valid_bst(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.is_valid_bst(root)


def assert_is_valid_bst(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
