import pytest

from leetcode_py import logged_test

from .helpers import assert_first_bad_version, run_first_bad_version
from .solution import Solution


class TestFirstBadVersion:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, bad, expected",
        [
            (5, 4, 4),
            (1, 1, 1),
            (3, 1, 1),
            (10, 7, 7),
            (100, 50, 50),
            (2, 1, 1),
            (2, 2, 2),
            (1000, 1, 1),
            (1000, 999, 999),
            (1000, 500, 500),
            (20, 15, 15),
            (50, 25, 25),
            (8, 3, 3),
            (16, 9, 9),
            (200, 150, 150),
        ],
    )
    def test_first_bad_version(self, n: int, bad: int, expected: int):
        result = run_first_bad_version(Solution, n, bad)
        assert_first_bad_version(result, expected)
