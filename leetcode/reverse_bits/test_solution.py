import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_bits, run_reverse_bits
from .solution import Solution


class TestReverseBits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (43261596, 964176192),
            (2147483644, 1073741822),
            (0, 0),
            (1, 2147483648),
            (2, 1073741824),
            (3, 3221225472),
            (4, 536870912),
            (5, 2684354560),
            (6, 1610612736),
            (7, 3758096384),
            (8, 268435456),
            (9, 2415919104),
            (10, 1342177280),
            (11, 3489660928),
            (12, 805306368),
            (13, 2952790016),
        ],
    )
    def test_reverse_bits(self, n: int, expected: int):
        result = run_reverse_bits(Solution, n)
        assert_reverse_bits(result, expected)
