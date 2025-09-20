import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_nth_from_end, run_remove_nth_from_end
from .solution import Solution


class TestRemoveNthNodeFromEndOfList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, n, expected",
        [
            ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
            ([1], 1, []),
            ([1, 2], 1, [1]),
            ([1, 2], 2, [2]),
            ([1, 2, 3], 3, [2, 3]),
            ([1, 2, 3], 1, [1, 2]),
            ([1, 2, 3, 4], 2, [1, 2, 4]),
            ([1, 2, 3, 4], 4, [2, 3, 4]),
            ([5], 1, []),
            ([10, 20], 1, [10]),
            ([10, 20], 2, [20]),
            ([1, 2, 3, 4, 5, 6], 3, [1, 2, 3, 5, 6]),
            ([7, 8, 9, 10], 1, [7, 8, 9]),
            ([100], 1, []),
            ([1, 2, 3, 4, 5, 6, 7], 4, [1, 2, 3, 5, 6, 7]),
            ([0, 1, 2], 2, [0, 2]),
            ([50, 60, 70, 80, 90], 5, [60, 70, 80, 90]),
            ([25, 35], 1, [25]),
        ],
    )
    def test_remove_nth_from_end(self, head_list: list[int], n: int, expected: list[int]):
        result = run_remove_nth_from_end(Solution, head_list, n)
        assert_remove_nth_from_end(result, expected)
