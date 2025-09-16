import pytest

from leetcode_py import logged_test

from .helpers import assert_diameter_of_binary_tree, run_diameter_of_binary_tree
from .solution import Solution


class TestDiameterOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, 4, 5], 3),
            ([1, 2], 1),
            ([], 0),
            ([1], 0),
            ([1, 2, 3], 2),
            ([1, None, 2], 1),
            ([1, 2, 3, 4, 5, None, None, 6, 7], 4),
            ([4, 2, 6, 1, 3, 5, 7], 4),
            ([1, 2, None, 3, None, 4], 3),
            ([1, 2, 3, None, None, 4, 5, None, None, 6, 7], 4),
            ([10, 5, 15, 3, 7, 12, 20], 4),
            ([1, None, 2, None, 3, None, 4], 3),
        ],
    )
    def test_diameter_of_binary_tree(self, root_list: list[int | None], expected: int):
        result = run_diameter_of_binary_tree(Solution, root_list)
        assert_diameter_of_binary_tree(result, expected)
