import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_invert_tree, create_tree, run_invert_tree
from .solution import Solution, SolutionBFS, SolutionDFS


class TestInvertBinaryTree:
    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
        ],
    )
    def test_invert_tree(
        self, root_list: list[int | None], expected_list: list[int | None], solution_class: type
    ):
        result = run_invert_tree(solution_class, root_list)
        expected = create_tree(expected_list)
        assert_invert_tree(result, expected)
