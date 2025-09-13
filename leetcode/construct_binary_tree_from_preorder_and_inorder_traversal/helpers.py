from leetcode_py import TreeNode


def run_build_tree(solution_class: type, preorder: list[int], inorder: list[int]):
    implementation = solution_class()
    return implementation.build_tree(preorder, inorder)


def assert_build_tree(result: TreeNode | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode.from_list(expected_list) if expected_list else None
    assert result == expected
    return True
