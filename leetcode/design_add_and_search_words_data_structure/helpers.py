from typing import Any


def run_word_dictionary(solution_class: type, operations: list[str], inputs: list[list[str]]):
    wd: Any = None
    results: list[bool | None] = []

    for op, args in zip(operations, inputs):
        if op == "WordDictionary":
            wd = solution_class()
            results.append(None)
        elif op == "addWord":
            assert wd is not None
            wd.add_word(args[0])
            results.append(None)
        elif op == "search":
            assert wd is not None
            results.append(wd.search(args[0]))

    return results


def assert_word_dictionary(result: list[bool | None], expected: list[bool | None]) -> bool:
    assert result == expected
    return True
