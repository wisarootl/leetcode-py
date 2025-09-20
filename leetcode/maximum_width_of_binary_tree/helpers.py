from leetcode_py import TreeNode


def run_width_of_binary_tree(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.width_of_binary_tree(root)


def assert_width_of_binary_tree(result: int, expected: int) -> bool:
    assert result == expected
    return True
