import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_middle_node, run_middle_node
from .solution import Solution


class TestMiddleOfTheLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected_list",
        [
            ([1, 2, 3, 4, 5], [3, 4, 5]),
            ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
            ([1], [1]),
            ([1, 2], [2]),
            ([1, 2, 3], [2, 3]),
            ([1, 2, 3, 4], [3, 4]),
            ([10, 20, 30, 40, 50, 60, 70], [40, 50, 60, 70]),
        ],
    )
    def test_middle_node(self, head_list: list[int], expected_list: list[int]):
        result = run_middle_node(Solution, head_list)
        assert_middle_node(result, expected_list)
