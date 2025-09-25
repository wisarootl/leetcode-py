import pytest

from leetcode_py import logged_test

from .helpers import assert_num_decodings, run_num_decodings
from .solution import Solution


class TestDecodeWays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("12", 2),
            ("226", 3),
            ("06", 0),
            ("0", 0),
            ("10", 1),
            ("27", 1),
            ("101", 1),
            ("100", 0),
            ("110", 1),
            ("2101", 1),
            ("2611055971756562", 4),
            ("1", 1),
            ("30", 0),
        ],
    )
    def test_num_decodings(self, s: str, expected: int):
        result = run_num_decodings(Solution, s)
        assert_num_decodings(result, expected)
