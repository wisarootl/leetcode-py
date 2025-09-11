from leetcode_py import TreeNode


def run_level_order(solution_class: type, root_list: list[int | None]):
    implementation = solution_class()
    root = TreeNode.from_list(root_list) if root_list else None
    return implementation.level_order(root)


def assert_level_order(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
