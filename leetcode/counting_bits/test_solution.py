import pytest

from leetcode_py import logged_test

from .helpers import assert_count_bits, run_count_bits
from .solution import Solution


class TestTestCountingBits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, n, expected",
        [
            (Solution, 2, [0, 1, 1]),
            (Solution, 5, [0, 1, 1, 2, 1, 2]),
            (Solution, 0, [0]),
            (Solution, 1, [0, 1]),
            (Solution, 3, [0, 1, 1, 2]),
            (Solution, 4, [0, 1, 1, 2, 1]),
            (Solution, 6, [0, 1, 1, 2, 1, 2, 2]),
            (Solution, 7, [0, 1, 1, 2, 1, 2, 2, 3]),
            (Solution, 8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
            (Solution, 9, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2]),
            (Solution, 10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
            (Solution, 15, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]),
            (Solution, 16, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]),
        ],
    )
    def test_count_bits(self, solution_class, n: int, expected: list[int]):
        result = run_count_bits(solution_class, n)
        assert_count_bits(result, expected)
