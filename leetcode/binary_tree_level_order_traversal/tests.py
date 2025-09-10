import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestBinaryTreeLevelOrderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
            ([1], [[1]]),
            ([], []),
            ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
            ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]),
            # Edge cases
            ([1, None, 2, None, 3], [[1], [2], [3]]),  # Right skewed
            ([1, 2, None, 3, None], [[1], [2], [3]]),  # Left skewed
            ([0], [[0]]),  # Single zero node
            ([-1, -2, -3], [[-1], [-2, -3]]),  # Negative values
            ([1, 2, 3, None, None, None, 4], [[1], [2, 3], [4]]),  # Sparse tree
            (
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
                [[5], [4, 8], [11, 13, 4], [7, 2, 1]],
            ),  # Complex tree
            ([1, 2, 2, 3, 3, 3, 3], [[1], [2, 2], [3, 3, 3, 3]]),  # Duplicate values
            ([1, None, None], [[1]]),  # Single node with null children
        ],
    )
    @logged_test
    def test_level_order(self, root_list: list[int | None], expected: list[list[int]]):
        root = TreeNode.from_list(root_list) if root_list else None
        result = self.solution.level_order(root)
        assert result == expected
