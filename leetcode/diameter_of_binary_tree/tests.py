import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestDiameterOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, 4, 5], 3),
            ([1, 2], 1),
            ([1], 0),
            ([], 0),
            ([1, 2, 3, 4, 5, None, None, 6, 7], 4),
            ([1, None, 2, None, 3, None, 4], 3),
            ([1, 2, None, 3, None, 4], 3),
            ([1, 2, 3], 2),
            ([1, 2, 3, 4, None, None, 5], 4),
        ],
    )
    @logged_test
    def test_diameter_of_binary_tree(self, root_list: list[int | None], expected: int):
        root = TreeNode.from_list(root_list)
        result = self.solution.diameter_of_binary_tree(root)
        assert result == expected
