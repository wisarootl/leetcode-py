import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_build_tree, run_build_tree
from .solution import Solution


class TestConstructBinaryTreeFromPreorderAndInorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "preorder, inorder, expected_list",
        [
            ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
            ([-1], [-1], [-1]),
            ([1, 2], [2, 1], [1, 2]),
            ([1, 2], [1, 2], [1, None, 2]),
            ([1, 2, 3], [2, 1, 3], [1, 2, 3]),
            ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
            ([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3], [1, 2, 3, 4, 5, 6]),
            ([1], [1], [1]),
            ([1, 2, 3, 4], [1, 2, 3, 4], [1, None, 2, None, 3, None, 4]),
            ([4, 3, 2, 1], [1, 2, 3, 4], [4, 3, None, 2, None, 1]),
            ([10, 5, 1, 7, 40, 50], [1, 5, 7, 10, 40, 50], [10, 5, 40, 1, 7, None, 50]),
        ],
    )
    def test_build_tree(self, preorder: list[int], inorder: list[int], expected_list: list[int | None]):
        result = run_build_tree(Solution, preorder, inorder)
        assert_build_tree(result, expected_list)
