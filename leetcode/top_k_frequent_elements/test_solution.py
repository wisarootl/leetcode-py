import pytest

from leetcode_py import logged_test

from .helpers import assert_top_k_frequent, run_top_k_frequent
from .solution import Solution


class TestTestTopKFrequentElements:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, nums, k, expected",
        [
            (Solution, [1, 1, 1, 2, 2, 3], 2, [1, 2]),
            (Solution, [1], 1, [1]),
            (Solution, [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
            (Solution, [1, 2, 3, 4, 5], 1, [1]),
            (Solution, [1, 1, 2, 2, 3, 3], 3, [1, 2, 3]),
            (Solution, [1, 1, 1, 1, 1], 1, [1]),
            (Solution, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [1, 2, 3, 4, 5]),
            (Solution, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2, [1, 2]),
            (Solution, [1, 2, 3, 1, 2, 3, 1, 2, 3], 3, [1, 2, 3]),
            (Solution, [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4], 4, [1, 2, 3, 4]),
            (Solution, [1, 1, 1, 1, 2, 2, 2, 3, 3, 4], 3, [1, 2, 3]),
            (
                Solution,
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
                5,
                [1, 2, 3, 4, 5],
            ),
            (Solution, [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5], 3, [1, 2, 3]),
        ],
    )
    def test_top_k_frequent(self, solution_class, nums: list[int], k: int, expected: list[int]):
        result = run_top_k_frequent(solution_class, nums, k)
        assert_top_k_frequent(result, expected)
