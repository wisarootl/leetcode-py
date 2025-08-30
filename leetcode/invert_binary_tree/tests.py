import pytest
from loguru import logger

from leetcode_py.test_utils import logged_test
from leetcode_py.tree_node import TreeNode

from .solution import Solution


class TestInvertBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "input_arr, expected_arr",
        [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
            ([1], [1]),
            ([1, 2], [1, None, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
            ([3, 9, 20, None, None, 15, 7], [3, 20, 9, 7, 15]),
        ],
    )
    @logged_test
    def test_invert_tree(self, input_arr: list[int | None], expected_arr: list[int | None]):
        logger.info(f"Testing with input: {input_arr}")
        root = TreeNode.from_list(input_arr)
        if root:
            logger.debug(f"Input tree:\n{root}")

        result = self.solution.invert_tree(root)
        result_arr = result.to_list() if result else []

        if result:
            logger.debug(f"Result tree:\n{result}")
        logger.success(f"Got result: {result_arr}")
        assert result_arr == expected_arr
