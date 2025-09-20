import pytest

from leetcode_py import logged_test

from .helpers import assert_odd_even_list, run_odd_even_list
from .solution import Solution


class TestOddEvenLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected",
        [
            ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
            ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
            ([], []),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, 2, 3], [1, 3, 2]),
            ([1, 2, 3, 4], [1, 3, 2, 4]),
            ([5, 4, 3, 2, 1], [5, 3, 1, 4, 2]),
            ([10, 20, 30, 40, 50, 60], [10, 30, 50, 20, 40, 60]),
            ([7, 6, 5, 4, 3, 2, 1], [7, 5, 3, 1, 6, 4, 2]),
            ([100], [100]),
            ([1, 3, 5, 7, 9], [1, 5, 9, 3, 7]),
            ([2, 4, 6, 8], [2, 6, 4, 8]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 7, 5, 3, 1, 8, 6, 4, 2]),
            ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
            ([-1, -2, -3, -4, -5], [-1, -3, -5, -2, -4]),
        ],
    )
    def test_odd_even_list(self, head_list: list[int], expected: list[int]):
        result = run_odd_even_list(Solution, head_list)
        assert_odd_even_list(result, expected)
