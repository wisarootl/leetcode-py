from leetcode_py import TreeNode


def run_right_side_view(solution_class: type, root_list: list[int | None]):
    implementation = solution_class()
    root = TreeNode.from_list(root_list) if root_list else None
    return implementation.right_side_view(root)


def assert_right_side_view(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
