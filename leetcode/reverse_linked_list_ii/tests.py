import pytest
from loguru import logger

from leetcode_py.list_node import ListNode
from leetcode_py.test_utils import logged_test

from .solution import Solution


class TestReverseLinkedListII:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize(
        "head_list, left, right, expected_list",
        [
            ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            ([5], 1, 1, [5]),
            ([1, 2, 3], 1, 3, [3, 2, 1]),
        ],
    )
    @logged_test
    def test_reverse_between(
        self, head_list: list[int], left: int, right: int, expected_list: list[int]
    ):
        logger.info(f"Testing with head_list={head_list}, left={left}, right={right}")
        head = ListNode.from_list(head_list)
        expected = ListNode.from_list(expected_list)
        result = self.solution.reverse_between(head, left, right)
        logger.success(f"Got result: {result.to_list() if result else []}")
        assert result == expected
