import pytest

from leetcode_py.test_utils import logged_test

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
        ],
    )
    def test_min_stack(self, operations: list[str], inputs: list[list[int]], expected: list[int | None]):
        result = run_min_stack_operations(MinStack, operations, inputs)
        assert_min_stack_operations(result, expected)
