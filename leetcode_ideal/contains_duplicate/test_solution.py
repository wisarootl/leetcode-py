import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_contains_duplicate, run_contains_duplicate
from .solution import Solution


class TestContainsDuplicate:

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
            ([], False),
            ([1], False),
            ([1, 1], True),
            ([-1, -2, -3, -1], True),
            ([-1, -2, -3, -4], False),
            ([0, 0], True),
            ([1000000, 999999, 1000000], True),
            (list(range(1000)), False),
            ([1] * 1000, True),
        ],
    )
    def test_contains_duplicate(self, nums: list[int], expected: bool):
        result = run_contains_duplicate(Solution, nums)
        assert_contains_duplicate(result, expected)
