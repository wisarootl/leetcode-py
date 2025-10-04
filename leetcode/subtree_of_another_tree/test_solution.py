import pytest

from leetcode_py import logged_test

from .helpers import assert_is_subtree, run_is_subtree
from .solution import Solution


class TestSubtreeOfAnotherTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, sub_root_list, expected",
        [
            ([3, 4, 5, 1, 2], [4, 1, 2], True),
            ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
            ([1], [1], True),
            ([1], [2], False),
            ([1, 2, 3], [2], True),
            ([1, 2, 3], [2, 4], False),
            ([1, 2, 3, 4, 5], [2, 4, 5], True),
            ([1, 2, 3, 4, 5], [2, 4, 6], False),
            ([1, 2, 3, 4, 5, 6, 7], [2, 4, 5], True),
            ([1, 2, 3, 4, 5, 6, 7], [3, 6, 7], True),
            ([1, 2, 3, 4, 5, 6, 7], [2, 4, 6], False),
            ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4], False),
            ([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7], False),
            ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], True),
        ],
    )
    def test_is_subtree(
        self,
        root_list: list[int | None],
        sub_root_list: list[int | None],
        expected: bool,
    ):
        result = run_is_subtree(Solution, root_list, sub_root_list)
        assert_is_subtree(result, expected)
