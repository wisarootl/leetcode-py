import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestCoinChange:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "coins, amount, expected",
        [
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
            ([1], 0, 0),
            ([1, 3, 4], 6, 2),
            ([2, 5, 10, 1], 27, 4),
            ([10, 1, 2, 5], 27, 4),
            ([5], 3, -1),
            ([5, 2], 3, -1),
            ([1], 1, 1),
            ([1, 2], 2, 1),
            ([186, 419, 83, 408], 6249, 20),
        ],
    )
    @logged_test
    def test_coin_change(self, coins: list[int], amount: int, expected: int):
        result = self.solution.coin_change(coins, amount)
        assert result == expected
