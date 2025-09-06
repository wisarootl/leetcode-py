import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestMaximumDepthOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "root_list, expected",
        [
            # Original examples
            ([3, 9, 20, None, None, 15, 7], 3),
            ([1, None, 2], 2),
            ([], 0),
            # Single node
            ([1], 1),
            # Left skewed tree (depth 3)
            ([1, 2, None, 3], 3),
            # Right skewed tree (depth 2)
            ([1, None, 2], 2),
            # Balanced tree
            ([1, 2, 3, 4, 5, 6, 7], 3),
            # Unbalanced tree (left heavy)
            ([1, 2, 3, 4, 5, None, None, 6, 7], 4),
            # Two nodes
            ([1, 2], 2),
            ([1, None, 2], 2),
        ],
    )
    @logged_test
    def test_max_depth(self, root_list: list[int | None], expected: int):
        root = TreeNode.from_list(root_list)
        result = self.solution.max_depth(root)
        assert result == expected
