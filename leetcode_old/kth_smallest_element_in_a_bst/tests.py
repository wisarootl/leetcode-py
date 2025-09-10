import pytest

from leetcode_py import TreeNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestKthSmallestElementInABst:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "root_list, k, expected",
        [([3, 1, 4, None, 2], 1, 1), ([5, 3, 6, 2, 4, None, None, 1], 3, 3), ([1], 1, 1)],
    )
    @logged_test
    def test_kth_smallest(self, root_list: list[int | None], k: int, expected: int):
        root = TreeNode.from_list(root_list)
        result = self.solution.kth_smallest(root, k)
        assert result == expected
