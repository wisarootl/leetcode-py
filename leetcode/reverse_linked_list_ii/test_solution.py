import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_between, run_reverse_between
from .solution import Solution


class TestReverseLinkedListII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, left, right, expected_list",
        [
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            ([5], 1, 1, [5]),
            ([1, 2], 1, 2, [2, 1]),
            ([1, 2, 3], 1, 3, [3, 2, 1]),
            ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
            ([1, 2, 3, 4, 5], 3, 3, [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4], 2, 3, [1, 3, 2, 4]),
            ([1, 2, 3, 4, 5, 6], 3, 5, [1, 2, 5, 4, 3, 6]),
            ([10], 1, 1, [10]),
            ([1, 2, 3, 4, 5, 6, 7], 1, 7, [7, 6, 5, 4, 3, 2, 1]),
            ([3, 5], 1, 1, [3, 5]),
            ([7, 9, 2, 10, 1, 8, 6], 4, 6, [7, 9, 2, 8, 1, 10, 6]),
        ],
    )
    def test_reverse_between(
        self, head_list: list[int], left: int, right: int, expected_list: list[int]
    ):
        result = run_reverse_between(Solution, head_list, left, right)
        assert_reverse_between(result, expected_list)
