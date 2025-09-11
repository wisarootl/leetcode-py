import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_max_profit, run_max_profit
from .solution import Solution


class TestBestTimeToBuyAndSellStock:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "prices, expected",
        [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([1, 2, 3, 4, 5], 4),
            ([5, 4, 3, 2, 1], 0),
            ([1], 0),
            ([2, 1], 0),
            ([1, 2], 1),
            ([3, 2, 6, 5, 0, 3], 4),
        ],
    )
    def test_max_profit(self, prices: list[int], expected: int):
        result = run_max_profit(Solution, prices)
        assert_max_profit(result, expected)
