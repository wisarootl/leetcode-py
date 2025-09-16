import pytest

from leetcode_py import logged_test

from .helpers import assert_lowest_common_ancestor, run_lowest_common_ancestor
from .solution import Solution


class TestLowestCommonAncestorOfABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, p_val, q_val, expected_val",
        [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
            ([1, 2], 1, 2, 1),
            ([2, 1], 2, 1, 2),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 7, 5),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 0, 8, 1),
            ([1, None, 2, None, 3], 2, 3, 2),
            ([4, 2, 6, 1, 3, 5, 7], 1, 7, 4),
            ([10, 5, 15, 3, 7, None, 18], 3, 7, 5),
            ([1, 2, 3, 4, 5, 6, 7], 4, 5, 2),
            ([20, 8, 22, 4, 12, None, 25], 4, 12, 8),
            ([50, 30, 70, 20, 40, 60, 80], 20, 40, 30),
        ],
    )
    def test_lowest_common_ancestor(
        self, root_list: list[int | None], p_val: int, q_val: int, expected_val: int
    ):
        result = run_lowest_common_ancestor(Solution, root_list, p_val, q_val)
        assert_lowest_common_ancestor(result, expected_val)
