from leetcode_py import TreeNode


def run_max_depth(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.max_depth(root)


def assert_max_depth(result: int, expected: int) -> bool:
    assert result == expected
    return True
