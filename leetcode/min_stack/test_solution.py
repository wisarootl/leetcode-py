import pytest

from leetcode_py import logged_test

from .helpers import assert_min_stack_operations, run_min_stack_operations
from .solution import MinStack


class TestTestMinStack:

    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                [[], [-2], [0], [-3], [], [], [], []],
                [None, None, None, None, -3, None, 0, -2],
            ),
            (
                ["MinStack", "push", "top", "getMin", "pop"],
                [[], [5], [], [], []],
                [None, None, 5, 5, None],
            ),
            (
                ["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
                [[], [1], [1], [2], [], [], [], [], []],
                [None, None, None, None, 1, None, 1, None, 1],
            ),
            (["MinStack", "push", "getMin", "top"], [[], [0], [], []], [None, None, 0, 0]),
            (
                ["MinStack", "push", "push", "getMin", "push", "getMin", "pop", "getMin"],
                [[], [2], [1], [], [0], [], [], []],
                [None, None, None, 1, None, 0, None, 1],
            ),
            (
                ["MinStack", "push", "push", "push", "top", "getMin", "pop", "pop", "top", "getMin"],
                [[], [3], [1], [4], [], [], [], [], [], []],
                [None, None, None, None, 4, 1, None, None, 3, 3],
            ),
            (
                ["MinStack", "push", "push", "getMin", "pop", "push", "getMin"],
                [[], [-1], [-2], [], [], [0], []],
                [None, None, None, -2, None, None, -1],
            ),
            (
                ["MinStack", "push", "push", "push", "push", "getMin", "pop", "pop", "getMin"],
                [[], [5], [3], [7], [2], [], [], [], []],
                [None, None, None, None, None, 2, None, None, 3],
            ),
            (
                [
                    "MinStack",
                    "push",
                    "push",
                    "push",
                    "getMin",
                    "pop",
                    "getMin",
                    "pop",
                    "getMin",
                    "pop",
                    "push",
                    "getMin",
                ],
                [[], [10], [5], [15], [], [], [], [], [], [], [8], []],
                [None, None, None, None, 5, None, 5, None, 10, None, None, 8],
            ),
            (
                [
                    "MinStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "getMin",
                    "pop",
                    "getMin",
                    "pop",
                    "getMin",
                ],
                [[], [1], [2], [0], [3], [4], [], [], [], [], []],
                [None, None, None, None, None, None, 0, None, 0, None, 0],
            ),
            (
                ["MinStack", "push", "getMin", "push", "getMin", "push", "getMin", "top"],
                [[], [2147483647], [], [-2147483648], [], [0], [], []],
                [None, None, 2147483647, None, -2147483648, None, -2147483648, 0],
            ),
            (
                [
                    "MinStack",
                    "push",
                    "push",
                    "push",
                    "push",
                    "push",
                    "top",
                    "getMin",
                    "pop",
                    "top",
                    "getMin",
                    "pop",
                    "getMin",
                ],
                [[], [1], [1], [1], [1], [1], [], [], [], [], [], [], []],
                [None, None, None, None, None, None, 1, 1, None, 1, 1, None, 1],
            ),
        ],
    )
    def test_min_stack(self, operations: list[str], inputs: list[list[int]], expected: list[int | None]):
        result = run_min_stack_operations(MinStack, operations, inputs)
        assert_min_stack_operations(result, expected)
