import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestBestTimeToBuyAndSellStock:
    def setup_method(self):
        self.solution = Solution()

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
    @logged_test
    def test_max_profit(self, prices: list[int], expected: int):
        result = self.solution.max_profit(prices)
        assert result == expected
