import pytest

from leetcode_py.test_utils import logged_test

from .solution import MinStack


class TestMinStack:
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
            (
                ["MinStack", "push", "push", "getMin", "push", "getMin", "pop", "getMin"],
                [[], [3], [1], [], [0], [], [], []],
                [None, None, None, 1, None, 0, None, 1],
            ),
        ],
    )
    @logged_test
    def test_min_stack(self, operations: list[str], inputs: list[list[int]], expected: list[int | None]):
        stack: MinStack | None = None
        results: list[int | None] = []
        for i, op in enumerate(operations):
            if op == "MinStack":
                stack = MinStack()
                results.append(None)
            elif op == "push" and stack is not None:
                stack.push(inputs[i][0])
                results.append(None)
            elif op == "pop" and stack is not None:
                stack.pop()
                results.append(None)
            elif op == "top" and stack is not None:
                results.append(stack.top())
            elif op == "getMin" and stack is not None:
                results.append(stack.get_min())
        assert results == expected
