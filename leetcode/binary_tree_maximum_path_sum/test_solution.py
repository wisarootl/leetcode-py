import pytest

from leetcode_py import logged_test

from .helpers import assert_max_path_sum, run_max_path_sum
from .solution import Solution


class TestBinaryTreeMaximumPathSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3], 6),
            ([-10, 9, 20, None, None, 15, 7], 42),
            ([1], 1),
            ([-3], -3),
            ([1, -2, 3], 4),
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48),
            ([1, 2, 3, 4, 5], 11),
            ([-1, -2, -3], -1),
            ([1, -1, 2], 3),
            ([1, 2, -3, 4, 5], 11),
            ([1, 2, 3, None, None, 4, 5], 12),
            ([-1, 2, 3], 4),
            ([1, -2, -3, 1, 3, -2, None, -1], 3),
            ([2, -1], 2),
            ([1, 2], 3),
        ],
    )
    def test_max_path_sum(self, root_list: list[int | None], expected: int):
        result = run_max_path_sum(Solution, root_list)
        assert_max_path_sum(result, expected)
