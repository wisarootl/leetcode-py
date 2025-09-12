import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_is_balanced, run_is_balanced
from .solution import Solution


class TestBalancedBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], True),
            ([1, 2, 2, 3, 3, None, None, 4, 4], False),
            ([], True),
            ([1], True),
            ([1, 2], True),
            ([1, None, 2], True),
            ([1, 2, 3, 4], True),
            ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], False),
            ([1, 2, 3], True),
            ([1, 2, None, 3], False),
            ([1, None, 2, None, 3], False),
            ([1, 2, 3, 4, 5, 6, 7], True),
            ([1, 2, 3, None, None, 4, None, None, 5], False),
            ([5, 1, 4, None, None, 3, 6], True),
            ([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None, 5, 5], True),
        ],
    )
    def test_is_balanced(self, root_list: list[int | None], expected: bool):
        result = run_is_balanced(Solution, root_list)
        assert_is_balanced(result, expected)
