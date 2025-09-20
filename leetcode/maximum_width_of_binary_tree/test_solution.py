import pytest

from leetcode_py import logged_test

from .helpers import assert_width_of_binary_tree, run_width_of_binary_tree
from .solution import Solution


class TestMaximumWidthOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 3, 2, 5, 3, None, 9], 4),
            ([1, 3, 2, 5, None, None, 9, 6, None, 7], 7),
            ([1, 3, 2, 5], 2),
            ([1], 1),
            ([1, 2], 1),
            ([1, None, 2], 1),
            ([1, 2, 3], 2),
            ([1, 2, 3, 4], 2),
            ([1, 2, 3, 4, 5], 2),
            ([1, 2, 3, None, None, 4, 5], 2),
            ([1, 2, 3, None, 4, None, 5], 3),
            ([1, 2, 3, 4, None, None, 5, 6], 4),
            ([1, None, 2, None, 3, None, 4], 1),
            ([1, 2, None, 3, None, 4], 1),
            ([1, 2, 3, 4, 5, 6, 7], 4),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 8),
        ],
    )
    def test_width_of_binary_tree(self, root_list: list[int | None], expected: int):
        result = run_width_of_binary_tree(Solution, root_list)
        assert_width_of_binary_tree(result, expected)
