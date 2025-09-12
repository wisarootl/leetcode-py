import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_lowest_common_ancestor, run_lowest_common_ancestor
from .solution import Solution


class TestLowestCommonAncestorOfABinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, p_val, q_val, expected_val",
        [
            ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
            ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
            ([2, 1], 2, 1, 2),
            ([2, 1], 1, 2, 2),
            ([6, 2, 8, 0, 4, 7, 9], 0, 4, 2),
            ([6, 2, 8, 0, 4, 7, 9], 7, 9, 8),
        ],
    )
    def test_lowest_common_ancestor(
        self, root_list: list[int | None], p_val: int, q_val: int, expected_val: int
    ):
        result = run_lowest_common_ancestor(Solution, root_list, p_val, q_val)
        assert_lowest_common_ancestor(result, expected_val)
