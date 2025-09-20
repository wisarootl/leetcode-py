import pytest

from leetcode_py import logged_test

from .helpers import assert_find_max_length, run_find_max_length
from .solution import Solution


class TestContiguousArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([0, 1], 2),
            ([0, 1, 0], 2),
            ([0, 1, 1, 1, 1, 1, 0, 0, 0], 6),
            ([0], 0),
            ([1], 0),
            ([0, 0], 0),
            ([1, 1], 0),
            ([0, 0, 1, 0, 0, 1, 1, 0], 6),
            ([1, 0, 1, 0, 1], 4),
            ([0, 1, 1, 0, 1, 1, 1, 0], 4),
            ([1, 1, 1, 1, 1, 1, 1, 1], 0),
            ([0, 0, 0, 0, 0, 0, 0, 0], 0),
            ([1, 0, 1, 1, 0, 0, 1, 0, 1], 8),
            ([0, 1, 0, 1, 0, 1, 0, 1], 8),
            ([1, 0, 0, 1, 1, 0, 1, 0, 0, 1], 10),
            ([0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0], 10),
            ([1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 8),
        ],
    )
    def test_find_max_length(self, nums: list[int], expected: int):
        result = run_find_max_length(Solution, nums)
        assert_find_max_length(result, expected)
