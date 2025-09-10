import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution, SolutionBFS, SolutionDFS


class TestBinaryTreeRightSideView:
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
            ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
            ([1, None, 3], [1, 3]),
            ([], []),
        ],
    )
    @logged_test
    def test_right_side_view(
        self,
        root_list: list[int | None],
        expected: list[int],
        solution_class: type[Solution | SolutionDFS | SolutionBFS],
    ):
        solution = solution_class()
        root = TreeNode.from_list(root_list)
        result = solution.right_side_view(root)
        assert result == expected
