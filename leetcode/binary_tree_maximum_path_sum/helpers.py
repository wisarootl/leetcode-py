from leetcode_py import TreeNode


def run_max_path_sum(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.max_path_sum(root)


def assert_max_path_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
