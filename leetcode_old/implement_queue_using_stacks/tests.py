import pytest

from leetcode_py.test_utils import logged_test

from .solution import MyQueue


class TestImplementQueueUsingStacks:
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
    @logged_test
    def test_queue_operations(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None | bool]
    ):
        queue = None
        results: list[int | None | bool] = []
        for i, op in enumerate(operations):
            if op == "MyQueue":
                queue = MyQueue()
                results.append(None)
            elif op == "push" and queue is not None:
                queue.push(inputs[i][0])
                results.append(None)
            elif op == "pop" and queue is not None:
                results.append(queue.pop())
            elif op == "peek" and queue is not None:
                results.append(queue.peek())
            elif op == "empty" and queue is not None:
                results.append(queue.empty())
        assert results == expected
