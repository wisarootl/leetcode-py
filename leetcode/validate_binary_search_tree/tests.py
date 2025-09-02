import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution, SolutionBFS, SolutionDFS


class TestValidateBinarySearchTree:
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([2, 1, 3], True),
            ([5, 1, 4, None, None, 3, 6], False),
            ([1], True),
            ([1, 1], False),
        ],
    )
    @logged_test
    def test_is_valid_bst(
        self,
        root_list: list[int | None],
        expected: bool,
        solution_class: type[Solution | SolutionDFS | SolutionBFS],
    ):
        solution = solution_class()
        root = TreeNode.from_list(root_list)
        result = solution.is_valid_bst(root)
        assert result == expected
