import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_is_valid_bst, run_is_valid_bst
from .solution import Solution, SolutionBFS, SolutionDFS


class TestValidateBinarySearchTree:

    @logged_test
    @pytest.mark.parametrize("solution_class", [Solution, SolutionDFS, SolutionBFS])
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([2, 1, 3], True),
            ([5, 1, 4, None, None, 3, 6], False),
            ([1], True),
            ([1, 1], False),
            ([10, 5, 15, None, None, 6, 20], False),
            ([2, 1, 3, None, None, None, 4], True),
        ],
    )
    def test_is_valid_bst(self, root_list: list[int | None], expected: bool, solution_class: type):
        result = run_is_valid_bst(solution_class, root_list)
        assert_is_valid_bst(result, expected)
