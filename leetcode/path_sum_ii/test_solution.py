import pytest

from leetcode_py import logged_test

from .helpers import assert_path_sum, run_path_sum
from .solution import Solution


class TestPathSumII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target_sum, expected",
        [
            (
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
                22,
                [[5, 4, 11, 2], [5, 8, 4, 5]],
            ),
            ([1, 2, 3], 5, []),
            ([1, 2], 0, []),
            ([], 0, []),
            ([1], 1, [[1]]),
            ([1], 0, []),
            ([1, 2, 3], 4, [[1, 3]]),
            (
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
                22,
                [[5, 4, 11, 2]],
            ),
            ([1, -2, -3, 1, 3, -2, None, -1], -1, [[1, -2, 1, -1]]),
            ([1, 2, 3, 4, 5], 7, [[1, 2, 4]]),
            ([2, 1, 3], 3, [[2, 1]]),
            ([1, 2, 3, 4, 5, 6, 7], 8, [[1, 2, 5]]),
        ],
    )
    def test_path_sum(self, root_list: list[int | None], target_sum: int, expected: list[list[int]]):
        result = run_path_sum(Solution, root_list, target_sum)
        assert_path_sum(result, expected)
