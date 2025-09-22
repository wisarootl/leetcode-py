import pytest

from leetcode_py import logged_test

from .helpers import assert_can_jump, run_can_jump
from .solution import Solution


class TestJumpGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, 1, 1, 4], True),
            ([3, 2, 1, 0, 4], False),
            ([0], True),
            ([1], True),
            ([1, 0], True),
            ([0, 1], False),
            ([2, 0, 0], True),
            ([1, 1, 1, 0], True),
            ([3, 0, 8, 2, 0, 0, 1], True),
            ([1, 0, 1, 0], False),
            ([2, 5, 0, 0], True),
            ([1, 2, 3], True),
            ([5, 4, 3, 2, 1, 0, 0], False),
            ([1, 1, 2, 2, 0, 1, 1], True),
            ([4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0], True),
        ],
    )
    def test_can_jump(self, nums: list[int], expected: bool):
        result = run_can_jump(Solution, nums)
        assert_can_jump(result, expected)
