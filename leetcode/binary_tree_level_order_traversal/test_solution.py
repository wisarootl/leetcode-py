import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_level_order, run_level_order
from .solution import Solution


class TestBinaryTreeLevelOrderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
            ([1], [[1]]),
            ([], []),
            ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
            ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]),
            ([1, None, 2, None, 3], [[1], [2], [3]]),
            ([1, 2, None, 3, None], [[1], [2], [3]]),
            ([0], [[0]]),
            ([-1, -2, -3], [[-1], [-2, -3]]),
            ([1, 2, 3, None, None, None, 4], [[1], [2, 3], [4]]),
            (
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
                [[5], [4, 8], [11, 13, 4], [7, 2, 1]],
            ),
            ([1, 2, 2, 3, 3, 3, 3], [[1], [2, 2], [3, 3, 3, 3]]),
            ([1, None, None], [[1]]),
        ],
    )
    def test_level_order(self, root_list: list[int | None], expected: list[list[int]]):
        result = run_level_order(Solution, root_list)
        assert_level_order(result, expected)
