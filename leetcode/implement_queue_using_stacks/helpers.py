def run_my_queue(solution_class: type, operations: list[str], inputs: list[list[int]]):
    queue = None
    results: list[int | None | bool] = []
    for i, op in enumerate(operations):
        if op == "MyQueue":
            queue = solution_class()
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
    return results, queue


def assert_my_queue(result: list[int | None | bool], expected: list[int | None | bool]) -> bool:
    assert result == expected
    return True
