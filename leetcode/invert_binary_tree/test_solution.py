import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_invert_tree, run_invert_tree
from .solution import Solution


class TestInvertBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
            ([1], [1]),
            ([1, 2], [1, None, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
            ([1, 2, 3, None, None, 4, 5], [1, 3, 2, 5, 4]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4]),
            ([5, 3, 8, 2, 4, 7, 9], [5, 8, 3, 9, 7, 4, 2]),
            ([10, 5, 15, None, 6, 12, 20], [10, 15, 5, 20, 12, 6]),
            ([1, 2, None, 3], [1, None, 2, None, 3]),
            ([0, -1, 1], [0, 1, -1]),
            ([100, 50, 150], [100, 150, 50]),
            ([1, 2, 3, None, 4, None, 5], [1, 3, 2, 5, None, 4]),
        ],
    )
    def test_invert_tree(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_invert_tree(Solution, root_list)
        assert_invert_tree(result, expected_list)
