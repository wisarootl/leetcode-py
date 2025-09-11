import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_has_cycle, run_has_cycle
from .solution import Solution


class TestLinkedListCycle:
    def setup_method(self):
        self.solution = Solution()

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
        ],
    )
    def test_has_cycle(self, values: list[int], pos: int, expected: bool):
        result = run_has_cycle(Solution, values, pos)
        assert_has_cycle(result, expected)
