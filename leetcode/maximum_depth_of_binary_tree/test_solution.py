import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_max_depth, run_max_depth
from .solution import Solution


class TestMaximumDepthOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], 3),
            ([1, None, 2], 2),
            ([], 0),
            ([1], 1),
            ([1, 2], 2),
            ([1, 2, 3], 2),
            ([1, 2, 3, 4], 3),
            ([1, None, 2, None, 3], 3),
            ([1, 2, 3, 4, 5, 6, 7], 3),
            ([1, 2, None, 4, None, None, None, 8], 3),
            ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 4),
            ([1, 2, 3, None, None, 4, 5, None, None, 6], 4),
            ([10], 1),
            ([1, 2, 2, 3, 3, 3, 3], 3),
            ([0, -1, 1, -2, -1, 0, 2], 3),
        ],
    )
    def test_max_depth(self, root_list: list[int | None], expected: int):
        result = run_max_depth(Solution, root_list)
        assert_max_depth(result, expected)
