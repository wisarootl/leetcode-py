import pytest
from loguru import logger

from leetcode_py.test_utils import logged_test
from leetcode_py.tree_node import TreeNode

from .solution import Solution, SolutionBFS, SolutionDFS

test_cases = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
    ([1], [1]),
    ([1, 2], [1, None, 2]),
    ([1, None, 2], [1, 2]),
    ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
    ([1, 2, 3, None, None, 4, 5], [1, 3, 2, 5, 4]),
]


class TestInvertBinaryTree:
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize("root_list, expected_list", test_cases)
    @logged_test
    def test_invert_tree(
        self,
        solution_class: type[Solution | SolutionDFS | SolutionBFS],
        root_list: list[int | None],
        expected_list: list[int | None],
    ):
        solution = solution_class()
        logger.info(f"Testing {solution_class.__name__} with root_list={root_list}")
        root = TreeNode.from_list(root_list)
        expected = TreeNode.from_list(expected_list)
        result = solution.invert_tree(root)
        logger.success(f"Got result: {result.to_list() if result else []}")
        assert result == expected
