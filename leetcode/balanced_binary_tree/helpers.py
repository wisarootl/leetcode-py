from leetcode_py import TreeNode


def run_is_balanced(solution_class: type, root_list: list[int | None]):
    implementation = solution_class()
    root = TreeNode.from_list(root_list)
    return implementation.is_balanced(root)


def assert_is_balanced(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
