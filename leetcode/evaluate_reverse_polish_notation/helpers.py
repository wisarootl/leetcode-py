def run_eval_rpn(solution_class: type, tokens: list[str]):
    implementation = solution_class()
    return implementation.eval_rpn(tokens)


def assert_eval_rpn(result: int, expected: int) -> bool:
    assert result == expected
    return True
