import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_majority_element, run_majority_element
from .solution import Solution


class TestMajorityElement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
            ([1], 1),
            ([1, 1, 2], 1),
            ([2, 2, 2, 1, 1], 2),
            ([5, 5, 5, 5, 1, 2, 3], 5),
            ([1, 2, 3, 4, 4, 4, 4], 4),
            ([0, 0, 0], 0),
            ([-1, -1, -1, 1, 1], -1),
        ],
    )
    def test_majority_element(self, nums: list[int], expected: int):
        result = run_majority_element(Solution, nums)
        assert_majority_element(result, expected)
