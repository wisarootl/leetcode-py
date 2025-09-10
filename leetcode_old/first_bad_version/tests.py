import pytest

from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestFirstBadVersion:

    @pytest.mark.parametrize(
        "n, bad, expected", [(5, 4, 4), (1, 1, 1), (3, 1, 1), (10, 7, 7), (5, -1, 1)]
    )
    @logged_test
    def test_first_bad_version(self, n: int, bad: int, expected: int):
        solution = Solution(first_bad=bad)
        result = solution.first_bad_version(n)
        assert result == expected
