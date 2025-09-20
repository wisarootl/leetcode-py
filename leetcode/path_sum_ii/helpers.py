from leetcode_py import TreeNode


def run_path_sum(solution_class: type, root_list: list[int | None], target_sum: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.path_sum(root, target_sum)


def assert_path_sum(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for comparison since order may vary
    result_sorted = sorted([sorted(path) for path in result])
    expected_sorted = sorted([sorted(path) for path in expected])
    assert result_sorted == expected_sorted
    return True
