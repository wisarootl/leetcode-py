import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_contains_duplicate, run_contains_duplicate
from .solution import Solution


class TestContainsDuplicate:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [([1, 2, 3, 1], True), ([1, 2, 3, 4], False), ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)],
    )
    def test_contains_duplicate(self, nums: list[int], expected: bool):
        result = run_contains_duplicate(Solution, nums)
        assert_contains_duplicate(result, expected)
