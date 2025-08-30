import pytest
from loguru import logger

from leetcode_py.test_utils import logged_test
from leetcode_py.tree_node import TreeNode

from .solution import Solution


class TestInvertBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
        ],
    )
    @logged_test
    def test_invert_tree(self, root_list: list[int | None], expected_list: list[int | None]):
        logger.info(f"Testing with root_list={root_list}")
        root = TreeNode.from_list(root_list)
        expected = TreeNode.from_list(expected_list)
        result = self.solution.invert_tree(root)
        logger.success(f"Got result: {result.to_list() if result else []}")
        assert result == expected
