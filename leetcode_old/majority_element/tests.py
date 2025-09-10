import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMajorityElement:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2), ([1], 1), ([1, 1, 2], 1), ([2, 2, 2, 1, 1], 2)],
    )
    @logged_test
    def test_majority_element(self, nums: list[int], expected: int):
        result = self.solution.majority_element(nums)
        assert result == expected
