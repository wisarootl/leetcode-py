from leetcode_py import TreeNode


def run_diameter_of_binary_tree(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.diameter_of_binary_tree(root)


def assert_diameter_of_binary_tree(result: int, expected: int) -> bool:
    assert result == expected
    return True
