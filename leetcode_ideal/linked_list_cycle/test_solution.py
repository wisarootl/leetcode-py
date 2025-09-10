import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_has_cycle, run_has_cycle
from .solution import Solution


class TestLinkedListCycle:

    @logged_test
    @pytest.mark.parametrize(
        "values, pos, expected",
        [
            ([3, 2, 0, -4], 1, True),
            ([1, 2], 0, True),
            ([1], -1, False),
            ([], -1, False),
            ([1, 2, 3], -1, False),
            ([1, 2, 3, 4, 5], 0, True),
            ([1, 2, 3, 4, 5], 2, True),
            ([1, 2, 3, 4, 5], 4, True),
            ([1], 0, True),
            ([1, 2], 1, True),
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, True),
            ([1, 2, 3, 4, 5, 6, 7, 8], -1, False),
            ([1, 2], -1, False),
            ([5, 10], 0, True),
            ([5, 10], 1, True),
            ([0], -1, False),
            ([-1, -2, -3], 1, True),
            ([100, 200, 300], 0, True),
        ],
    )
    def test_has_cycle(self, values: list[int], pos: int, expected: bool):

        result = run_has_cycle(Solution, values, pos)
        assert_has_cycle(result, expected)
