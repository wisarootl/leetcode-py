import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_is_valid_bst, run_is_valid_bst
from .solution import Solution


class TestValidateBinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([2, 1, 3], True),
            ([5, 1, 4, None, None, 3, 6], False),
            ([1], True),
            ([1, 1], False),
            ([10, 5, 15, None, None, 6, 20], False),
            ([2, 1, 3, None, None, None, 4], True),
            ([0], True),
            ([2147483647], True),
            ([-2147483648], True),
            ([5, 4, 6, None, None, 3, 7], False),
            ([10, 5, 15, None, None, 12, 20, None, None, None, None, 6, 25], True),
            ([3, 1, 5, 0, 2, 4, 6], True),
        ],
    )
    def test_is_valid_bst(self, root_list: list[int | None], expected: bool):
        result = run_is_valid_bst(Solution, root_list)
        assert_is_valid_bst(result, expected)
