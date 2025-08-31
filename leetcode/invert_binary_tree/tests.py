import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution, SolutionBFS, SolutionDFS


class TestInvertBinaryTree:
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]), ([2, 1, 3], [2, 3, 1]), ([], [])],
    )
    @logged_test
    def test_invert_tree(
        self,
        root_list: list[int | None],
        expected_list: list[int | None],
        solution_class: type[Solution | SolutionDFS | SolutionBFS],
    ):
        solution = solution_class()
        root = TreeNode.from_list(root_list)
        expected = TreeNode.from_list(expected_list)
        result = solution.invert_tree(root)
        assert result == expected
