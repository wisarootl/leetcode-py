import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestLowestCommonAncestorOfABinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    def _find_node(self, root: TreeNode[int] | None, val: int):
        if not root:
            return None
        if root.val == val:
            return root
        left = self._find_node(root.left, val)
        if left:
            return left
        return self._find_node(root.right, val)

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
    @logged_test
    def test_lowest_common_ancestor(
        self, root_list: list[int | None], p_val: int, q_val: int, expected_val: int
    ):
        root = TreeNode[int].from_list(root_list)
        assert root is not None
        p = self._find_node(root, p_val)
        q = self._find_node(root, q_val)
        assert p is not None and q is not None
        result = self.solution.lowest_common_ancestor(root, p, q)
        assert result is not None
        assert result.val == expected_val
