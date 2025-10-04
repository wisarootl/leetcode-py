import pytest

from leetcode_py import logged_test

from .helpers import assert_find_median_sorted_arrays, run_find_median_sorted_arrays
from .solution import Solution


class TestMedianOfTwoSortedArrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 3], [2], 2.0),
            ([1, 2], [3, 4], 2.5),
            ([1], [], 1.0),
            ([], [1], 1.0),
            ([1, 2, 3], [], 2.0),
            ([], [1, 2, 3], 2.0),
            ([1, 2, 3, 4], [], 2.5),
            ([], [1, 2, 3, 4], 2.5),
            ([1, 3, 5], [2, 4, 6], 3.5),
            ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], 6.0),
            ([1, 2, 3, 4, 5, 6, 7], [8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5, 6, 7, 8], [9, 10], 5.5),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [10], 5.5),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], 5.5),
            ([1, 1, 1, 1], [2, 2, 2, 2], 1.5),
            ([1, 1, 1, 1, 1], [2, 2, 2, 2], 1.0),
        ],
    )
    def test_find_median_sorted_arrays(self, nums1: list[int], nums2: list[int], expected: float):
        result = run_find_median_sorted_arrays(Solution, nums1, nums2)
        assert_find_median_sorted_arrays(result, expected)
