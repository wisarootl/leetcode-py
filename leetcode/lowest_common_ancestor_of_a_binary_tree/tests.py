import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestLowestCommonAncestorOfABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "root_list, p_val, q_val, expected_val",
        [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
            ([1, 2], 1, 2, 1),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 7, 5),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7, 4, 2),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 0, 8, 1),
            ([1], 1, 1, 1),
            ([2, 1, 3], 1, 3, 2),
            ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
            ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 3, 5, 4),
            ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0, 3, 2),
        ],
    )
    @logged_test
    def test_lowest_common_ancestor(
        self, root_list: list[int | None], p_val: int, q_val: int, expected_val: int
    ):
        root = TreeNode.from_list(root_list)
        assert root is not None
        p = root.find_node(p_val)
        q = root.find_node(q_val)
        assert p is not None and q is not None
        result = self.solution.lowest_common_ancestor(root, p, q)
        assert result is not None
        assert result.val == expected_val
