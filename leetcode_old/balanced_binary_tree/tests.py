import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestBalancedBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], True),
            ([1, 2, 2, 3, 3, None, None, 4, 4], False),
            ([], True),
            ([1], True),
            ([1, 2], True),
            ([1, None, 2], True),
            ([1, 2, 3], True),
            ([1, 2, None, 3], False),
            ([1, None, 2, None, 3], False),
            ([1, 2, 3, 4, 5, 6, 7], True),
            ([1, 2, 3, 4, None, None, 7, 8], False),
        ],
    )
    @logged_test
    def test_is_balanced(self, root_list: list[int | None], expected: bool):
        root = TreeNode.from_list(root_list)
        result = self.solution.is_balanced(root)
        assert result == expected
