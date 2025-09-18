import pytest

from leetcode_py import logged_test

from .helpers import assert_can_complete_circuit, run_can_complete_circuit
from .solution import Solution


class TestGasStation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "gas, cost, expected",
        [
            ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
            ([2, 3, 4], [3, 4, 3], -1),
            ([1, 2], [2, 1], 1),
            ([5], [4], 0),
            ([2], [2], 0),
            ([1, 2, 3], [3, 3, 3], -1),
            ([3, 1, 1], [1, 2, 2], 0),
            ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
            ([1, 2, 3, 4, 5, 5, 70], [2, 3, 4, 3, 9, 6, 2], 6),
            ([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9], -1),
            ([6, 1, 4, 3, 5], [3, 8, 2, 4, 2], 2),
            ([2, 3, 4, 5], [3, 4, 5, 6], -1),
        ],
    )
    def test_can_complete_circuit(self, gas: list[int], cost: list[int], expected: int):
        result = run_can_complete_circuit(Solution, gas, cost)
        assert_can_complete_circuit(result, expected)
