import pytest

from leetcode_py import logged_test

from .helpers import assert_hamming_weight, run_hamming_weight
from .solution import Solution


class TestNumberOf1Bits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (11, 3),
            (128, 1),
            (2147483645, 30),
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 1),
            (5, 2),
            (6, 2),
            (7, 3),
            (8, 1),
            (15, 4),
            (16, 1),
            (255, 8),
            (256, 1),
        ],
    )
    def test_hamming_weight(self, n: int, expected: int):
        result = run_hamming_weight(Solution, n)
        assert_hamming_weight(result, expected)
