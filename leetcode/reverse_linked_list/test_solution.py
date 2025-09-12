import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_reverse_list, run_reverse_list
from .solution import Solution


class TestReverseLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected_list",
        [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([1, 2], [2, 1]),
            ([1], [1]),
            ([], []),
            ([1, 2, 3], [3, 2, 1]),
            ([1, 2, 3, 4], [4, 3, 2, 1]),
            ([-1, -2, -3], [-3, -2, -1]),
            ([0], [0]),
            ([5000, -5000], [-5000, 5000]),
            ([1, 1, 1], [1, 1, 1]),
        ],
    )
    def test_reverse_list(self, head_list: list[int], expected_list: list[int]):
        result = run_reverse_list(Solution, head_list)
        assert_reverse_list(result, expected_list)
