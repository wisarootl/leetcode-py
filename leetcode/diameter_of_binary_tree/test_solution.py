import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_diameter_of_binary_tree, run_diameter_of_binary_tree
from .solution import Solution


class TestDiameterOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [([1, 2, 3, 4, 5], 3), ([1, 2], 1), ([], 0), ([1], 0), ([1, 2, 3], 2), ([1, None, 2], 1)],
    )
    def test_diameter_of_binary_tree(self, root_list: list[int | None], expected: int):
        result = run_diameter_of_binary_tree(Solution, root_list)
        assert_diameter_of_binary_tree(result, expected)
