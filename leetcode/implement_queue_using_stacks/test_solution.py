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
            (["MyQueue", "push", "peek", "pop"], [[], [5], [], []], [None, None, 5, 5]),
            (
                ["MyQueue", "push", "push", "pop", "push", "peek"],
                [[], [1], [2], [], [3], []],
                [None, None, None, 1, None, 2],
            ),
            (["MyQueue", "empty"], [[], []], [None, True]),
            (
                ["MyQueue", "push", "push", "push", "push", "pop", "pop", "pop", "pop", "empty"],
                [[], [1], [2], [3], [4], [], [], [], [], []],
                [None, None, None, None, None, 1, 2, 3, 4, True],
            ),
            (
                ["MyQueue", "push", "pop", "push", "pop", "empty"],
                [[], [7], [], [8], [], []],
                [None, None, 7, None, 8, True],
            ),
            (
                ["MyQueue", "push", "push", "peek", "peek", "pop", "peek"],
                [[], [9], [8], [], [], [], []],
                [None, None, None, 9, 9, 9, 8],
            ),
            (
                ["MyQueue", "push", "push", "push", "push", "push", "pop", "pop", "pop", "push", "peek"],
                [[], [1], [2], [3], [4], [5], [], [], [], [6], []],
                [None, None, None, None, None, None, 1, 2, 3, None, 4],
            ),
            (
                ["MyQueue", "push", "empty", "pop", "empty", "push", "empty"],
                [[], [1], [], [], [], [2], []],
                [None, None, False, 1, True, None, False],
            ),
            (
                ["MyQueue", "push", "push", "push", "pop", "push", "pop", "pop", "push", "pop"],
                [[], [1], [2], [3], [], [4], [], [], [5], []],
                [None, None, None, None, 1, None, 2, 3, None, 4],
            ),
        ],
    )
    def test_queue_operations(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None | bool]
    ):
        result, _ = run_my_queue(MyQueue, operations, inputs)
        assert_my_queue(result, expected)
