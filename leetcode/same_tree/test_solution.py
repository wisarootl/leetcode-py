import pytest

from leetcode_py import logged_test

from .helpers import assert_is_same_tree, run_is_same_tree
from .solution import Solution


class TestSameTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "p_list, q_list, expected",
        [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2], [1, None, 2], False),
            ([1, 2, 1], [1, 1, 2], False),
            ([], [], True),
            ([1], [1], True),
            ([1], [2], False),
            ([1, None, 2], [1, 2], False),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], False),
            ([1, 2, 3, None, 4], [1, 2, 3, None, 4], True),
            ([1, 2, 3, None, 4], [1, 2, 3, 4, None], False),
        ],
    )
    def test_is_same_tree(self, p_list: list[int | None], q_list: list[int | None], expected: bool):
        result = run_is_same_tree(Solution, p_list, q_list)
        assert_is_same_tree(result, expected)
