from leetcode_py import TreeNode


def create_tree(root_list: list[int | None]) -> TreeNode[int] | None:
    return TreeNode[int].from_list(root_list)


def run_invert_tree(solution_class: type, root_list: list[int | None]) -> TreeNode[int] | None:
    root = create_tree(root_list)
    return solution_class().invert_tree(root)


def assert_invert_tree(result: TreeNode[int] | None, expected: TreeNode[int] | None) -> bool:
    assert result == expected
    return True
