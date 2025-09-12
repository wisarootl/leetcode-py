import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_coin_change, run_coin_change
from .solution import Solution


class TestCoinChange:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "coins, amount, expected",
        [
            ([1, 2, 5], 11, 3),
            ([2], 3, -1),
            ([1], 0, 0),
            ([1, 3, 4], 6, 2),
            ([2, 5, 10, 1], 27, 4),
            ([5], 3, -1),
            ([1], 1, 1),
            ([1, 2], 2, 1),
            ([186, 419, 83, 408], 6249, 20),
        ],
    )
    def test_coin_change(self, coins: list[int], amount: int, expected: int):
        result = run_coin_change(Solution, coins, amount)
        assert_coin_change(result, expected)
