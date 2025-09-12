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
        ],
    )
    def test_max_depth(self, root_list: list[int | None], expected: int):
        result = run_max_depth(Solution, root_list)
        assert_max_depth(result, expected)
