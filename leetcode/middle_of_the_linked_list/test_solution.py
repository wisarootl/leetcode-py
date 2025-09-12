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
            ([5, 10], [10]),
            ([1, 3, 5, 7, 9], [5, 7, 9]),
            ([2, 4, 6, 8, 10, 12], [8, 10, 12]),
            ([100], [100]),
            ([7, 14, 21], [14, 21]),
            ([11, 22, 33, 44], [33, 44]),
            ([1, 1, 1, 1, 1], [1, 1, 1]),
        ],
    )
    def test_middle_node(self, head_list: list[int], expected_list: list[int]):
        result = run_middle_node(Solution, head_list)
        assert_middle_node(result, expected_list)
