import pytest

from leetcode_py import logged_test

from .helpers import assert_reorder_list, run_reorder_list
from .solution import Solution


class TestReorderList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected",
        [
            ([1, 2, 3, 4], [1, 4, 2, 3]),
            ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, 2, 3], [1, 3, 2]),
            ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 7, 2, 6, 3, 5, 4]),
            ([1, 2, 3, 4, 5, 6, 7, 8], [1, 8, 2, 7, 3, 6, 4, 5]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 9, 2, 8, 3, 7, 4, 6, 5]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]),
            (
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7],
            ),
            (
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                [1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7],
            ),
            (
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                [1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8],
            ),
            (
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8],
            ),
        ],
    )
    def test_reorder_list(self, head_list: list[int], expected: list[int]):
        result = run_reorder_list(Solution, head_list)
        assert_reorder_list(result, expected)
