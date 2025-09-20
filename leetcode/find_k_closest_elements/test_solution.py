import pytest

from leetcode_py import logged_test

from .helpers import assert_find_closest_elements, run_find_closest_elements
from .solution import Solution


class TestFindKClosestElements:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, k, x, expected",
        [
            ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
            ([1, 1, 2, 3, 4, 5], 4, -1, [1, 1, 2, 3]),
            ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
            ([1, 2, 3, 4, 5], 1, 3, [3]),
            ([1, 2, 3, 4, 5], 2, 3, [2, 3]),
            ([1, 2, 3, 4, 5], 3, 3, [2, 3, 4]),
            ([1, 2, 3, 4, 5], 5, 3, [1, 2, 3, 4, 5]),
            ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4]),
            ([1, 3], 1, 2, [1]),
            ([1, 3], 1, 3, [3]),
            ([1, 3], 2, 2, [1, 3]),
            ([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4, [0, 1, 1, 1, 2, 3, 6, 7, 8]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 5, [3, 4, 5, 6, 7]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 1, [1, 2, 3]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 10, [8, 9, 10]),
            ([-5, -3, -1, 0, 2, 4, 6], 4, 1, [-1, 0, 2, 4]),
            ([10], 1, 5, [10]),
            ([1, 2, 4, 5, 6, 6, 8, 9], 4, 6, [4, 5, 6, 6]),
        ],
    )
    def test_find_closest_elements(self, arr: list[int], k: int, x: int, expected: list[int]):
        result = run_find_closest_elements(Solution, arr, k, x)
        assert_find_closest_elements(result, expected)
