from typing import Any


def run_min_stack_operations(solution_class: type, operations: list[str], inputs: list[list[int]]):
    stack: Any = None
    results: list[int | None] = []
    for i, op in enumerate(operations):
        if op == "MinStack":
            stack = solution_class()
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
    return results


def assert_min_stack_operations(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
