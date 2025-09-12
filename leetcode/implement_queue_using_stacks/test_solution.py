import pytest

from leetcode_py.test_utils import logged_test

from .helpers import assert_my_queue, run_my_queue
from .solution import MyQueue


class TestImplementQueueUsingStacks:

    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MyQueue", "push", "push", "peek", "pop", "empty"],
                [[], [1], [2], [], [], []],
                [None, None, None, 1, 1, False],
            ),
            (
                ["MyQueue", "empty", "push", "peek", "pop", "empty"],
                [[], [], [1], [], [], []],
                [None, True, None, 1, 1, True],
            ),
            (
                ["MyQueue", "push", "push", "push", "pop", "pop", "peek", "pop", "empty"],
                [[], [1], [2], [3], [], [], [], [], []],
                [None, None, None, None, 1, 2, 3, 3, True],
            ),
        ],
    )
    def test_queue_operations(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None | bool]
    ):
        result, _ = run_my_queue(MyQueue, operations, inputs)
        assert_my_queue(result, expected)
