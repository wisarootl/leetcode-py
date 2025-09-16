import pytest

from leetcode_py import logged_test

from .helpers import assert_contains_duplicate, run_contains_duplicate
from .solution import Solution


class TestContainsDuplicate:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
            ([1], False),
            ([1, 1], True),
            ([0, 0], True),
            ([-1, -1], True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], False),
            ([1, 2, 3, 4, 5, 1], True),
            ([-1000000000, 1000000000, -1000000000], True),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0], True),
        ],
    )
    def test_contains_duplicate(self, nums: list[int], expected: bool):
        result = run_contains_duplicate(Solution, nums)
        assert_contains_duplicate(result, expected)
